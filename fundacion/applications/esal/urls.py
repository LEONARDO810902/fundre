from django.urls import path
from . import views

app_name = "esal_app"

urlpatterns = [
    path(
        'esal/',
        views.EsalListView.as_view(),
        name='listado-esal',
    ),
    path(
        'CreateEsal/',
        views.EsalCreateView.as_view(),
        name='create-esal',
    ),

]
