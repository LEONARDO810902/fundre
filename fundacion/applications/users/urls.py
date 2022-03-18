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
    path(
        'lista/',
        views.UserListView.as_view(),
        name='user-listado',
    ),
    path(
        'users/update/<pk>/',
        views.UserUpdateView.as_view(),
        name='user-update',
    ),
    path(
        'users/delete/<pk>/',
        views.UserDeleteView.as_view(),
        name='user-delete',
    ),
]
