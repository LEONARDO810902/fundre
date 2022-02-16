from django.shortcuts import render

# Create your views here.


from django.views.generic import (
    DetailView,
    ListView,

)

from .models import Entrada, Categoria


class EntradaListView(ListView):
    template_name = 'entrada/lista_entrada.html'
    context_object_name = 'entradas'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(EntradaListView, self).get_context_data(**kwargs)
        context["Categorias"] = Categoria.objects.all()
        return context

    def get_queryset(self):
        buscarentrada = self.request.GET.get("buscarentrada", '')
        categoria = self.request.GET.get("categoria", '')
        resultado = Entrada.objects.Buscar_entradas(
            buscarentrada, categoria)
        return resultado


class EntradaDetailView(DetailView):
    template_name = "entrada/detail.html"
    model = Entrada
