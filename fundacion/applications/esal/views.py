from pyexpat import model
from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    DetailView,
    ListView,
)

from .models import Esal


class EsalListView(ListView):
    template_name = "esal/esal_listado.html"
    context_object_name = 'listadoEsal'

    def get_queryset(self):
        return Esal.objects.Listado_esal_portada()
