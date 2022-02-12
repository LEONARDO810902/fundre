from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    CreateView,
)

from django.views.generic.edit import (
    FormView,
)

from .forms import UserCreateForm

from .models import User


class UserCreateView(FormView):
    template_name = 'users/create.html'
    form_class = UserCreateForm
    secess_url = '/'

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            form.cleaned_data['email'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero']
        )
        #
        return super(UserCreateView, self).form_valid(form)
