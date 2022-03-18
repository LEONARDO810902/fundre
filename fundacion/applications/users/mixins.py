from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


from .models import User


def check_ocupation_user(ocupation, user_ocupation):
    if (ocupation == User.ADMINISTRADOR or ocupation == user_ocupation):
        return True
    else:
        return False


class AdminpermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app.user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not check_ocupation_user(request.user.ocupation, User.ADMINISTRADOR):
            return HttpResponseRedirect(reverse('user_app.user-login'))
        return super().dispatch(request, *args, **kwargs)


class SecretariaPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app.user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.ocupation, User.SECRETARIA):
            return HttpResponseRedirect(reverse('user_app.user-login'))

        return super().dispatch(request, *args, **kwargs)


class TesoreroPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app.user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.ocupation, User.TESORERO):
            return HttpResponseRedirect(reverse('user_app.user-login'))

        return super().dispatch(request, *args, **kwargs)


class GerentePermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app.user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.ocupation, User.GERENTE):
            return HttpResponseRedirect(reverse('user_app.user-login'))

        return super().dispatch(request, *args, **kwargs)


class JuntaPermisoMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users_app.user-login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not check_ocupation_user(request.user.ocupation, User.JUNTA):
            return HttpResponseRedirect(reverse('user_app.user-login'))

        return super().dispatch(request, *args, **kwargs)
