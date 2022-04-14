import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

from applications.entrada.models import Entrada

# modelos de home
from .models import Home

# forms
from .forms import SuscribirseFoms, ContactoFoms


class homePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(homePageView, self).get_context_data(**kwargs)
        # Constexto de portada
        context["portada"] = Entrada.objects.entrada_en_portada()
        # contexto de modelo home page
        context["home"] = Home.objects.latest('created')
        # Constexto de home
        context["entradas_home"] = Entrada.objects.entrada_en_home()
        # Constexto de articulos recientes
        context["recientes_home"] = Entrada.objects.entrada_en_recientes()

        # Imagenes del carousel de portada
        context["corousel"] = Entrada.objects.entrada_corousel_home()

        # enviamos formulario de suscribe
        context["form"] = SuscribirseFoms
        return context


class SuscribeCreateView(CreateView):
    template_name = "home/suscribirme.html"
    form_class = SuscribirseFoms
    success_url = reverse_lazy('home_app:index')


class ContactoCreateView(CreateView):
    form_class = ContactoFoms
    success_url = '.'


class Error404View(TemplateView):
    template_name = 'home/errors/error_404.html'


class Error500View(TemplateView):
    template_name = 'home/errors/error_500.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r
        return view
