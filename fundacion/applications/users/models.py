from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Managers locales
from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    # TIPOS DE USUARIOS
    ADMINISTRADOR = '0'
    SECRETARIA = '1'
    TESORERO = '2'
    GERENTE = '3'
    JUNTA = '4'

    # GENEROS
    HOMBRE = 'M'
    MUJER = 'F'
    OTRO = 'O'

    OCUPATION_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (SECRETARIA, 'Secretario/a'),
        (TESORERO, 'Tesorero'),
        (GERENTE, 'Gerente'),
        (JUNTA, 'Junta'),
    ]

    GENDER_CHOICES = [
        (HOMBRE, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    ocupation = models.CharField(
        max_length=1, choices=OCUPATION_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
