from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/',
        views.UserPageView.as_view(),
        name='favorito-user',
    ),
    path(
        'agregar-entrada/<pk>',
        views.AgregarFavoritosView.as_view(),
        name='agregar-favoritos',
    ),
    path(
        'delete-favorito/<pk>',
        views.FavoritosDeleteView.as_view(),
        name='delete-favoritos',
    ),
]
