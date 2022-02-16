from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/',
        views.EntradaListView.as_view(),
        name='lista-entradas',
    ),
    path(
        'entradas/<pk>',
        views.EntradaDetailView.as_view(),
        name='edit-entradas',
    ),

]
