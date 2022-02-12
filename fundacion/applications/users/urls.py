from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'create/',
        views.UserCreateView.as_view(),
        name='usercreate'
    ),
]
