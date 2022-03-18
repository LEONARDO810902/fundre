import datetime

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.

from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.edit import (
    FormView,
)

from .forms import (
    UserCreateForm,
    LoginForm,
    UpdatePasswordForm,
    UserUpdateForm,
)

from applications.users.mixins import (
    AdminpermisoMixin
)

from .models import User


class FechaMixin(object):
    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now()
        return context

# DESARROLLO DE LOS DIFERENTES VIEWS


class UserCreateView(LoginRequiredMixin, FechaMixin, FormView):
    template_name = 'users/create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home_app:index')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            ocupation=form.cleaned_data['ocupation'],
        )
        #
        return super(UserCreateView, self).form_valid(form)


class LoginUsers(FechaMixin, FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUsers, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UserListView(AdminpermisoMixin, FechaMixin, ListView):
    template_name = 'users/lista.html'
    context_object_name = 'usuarios'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return User.objects.usuarios_sistema()


# ACTUALIZACION EN FORMULARIOS DE USUARIOS


class UpdatePasswordView(LoginRequiredMixin, FechaMixin, FormView):
    template_name = 'users/UpdateLogin.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )
        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


# ACUTLIZAR EL USUARIO


class UserUpdateView(UpdateView):
    template_name = 'users/update.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users_app:user-listado')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users_app:user-listado')
