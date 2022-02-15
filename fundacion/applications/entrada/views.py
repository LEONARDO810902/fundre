from django.shortcuts import render

# Create your views here.


from django.views.generic import (
    ListView,
)


class EntradaListView(ListView):
    template_name = 'entrada/lista_entrada.html'
    context_object_name = 'entradas'
    paginate_by = 10

    def get_queryset(self):
        return []
