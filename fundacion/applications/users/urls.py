from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'create/',
        views.UserCreateView.as_view(),
        name='user-create'
    ),
    path(
        'login/',
        views.LoginUsers.as_view(),
        name='user-login',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'PassUpdate/',
        views.UpdatePasswordView.as_view(),
        name='user-UpdatePassword',
    ),
]
