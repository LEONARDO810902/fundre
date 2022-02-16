from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.homePageView.as_view(),
        name='index',
    ),
    path(
        'registrar-suscribe',
        views.SuscribeCreateView.as_view(),
        name='home_suscribe',
    ),
    path(
        'contacto',
        views.ContactoCreateView.as_view(),
        name='home-contacto',
    ),
    path(
        'esal',
        views.EsalpageView.as_view(),
        name='home_esal',
    ),
]
