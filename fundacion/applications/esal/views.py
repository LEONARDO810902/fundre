
import datetime
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.

from django.views.generic import (
    DetailView,
    ListView,
)

from django.views.generic.edit import (
    FormView,
)

# MIXINS DE USERS
from applications.users.mixins import AdminpermisoMixin, TesoreroPermisoMixin

# Formularios locales de apps

from .forms import (
    EsalCreateForm,
)

from .models import Esal


class EsalListView(ListView):
    template_name = "esal/esal_listado.html"
    context_object_name = 'listadoEsal'

    def get_queryset(self):
        return Esal.objects.Listado_esal_portada()


class EsalCreateView(TesoreroPermisoMixin, FormView):
    template_name = "esal/esal_create.html"
    form_class = EsalCreateForm
    success_url = reverse_lazy('esal_app:listado-esal')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
