from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
from django.views.generic import (
    ListView,
    View,
    DeleteView
)

from applications.entrada.models import Entrada

from .models import Favoritos


class UserPageView(LoginRequiredMixin, ListView):
    template_name = "favoritos/perfil.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favoritos.objects.entradas_user(self.request.user)


class AgregarFavoritosView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        usuario = self.request.user
        entrada = Entrada.objects.get(id=self.kwargs['pk'])
        Favoritos.objects.create(
            user=usuario,
            entrada=entrada,
        )
        return HttpResponseRedirect(
            reverse(
                'favoritos_app:favorito-user'
            )
        )


class FavoritosDeleteView(DeleteView):
    model = Favoritos
    success_url = reverse_lazy('favoritos_app:favorito-user')
