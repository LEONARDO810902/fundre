from django.db import models
from django.conf import settings

# Create your models here.

# managers
from .managers import FovoritosManager


from model_utils.models import TimeStampedModel

from applications.entrada.models import Entrada


class Favoritos(TimeStampedModel):
    """Favoritos"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user_favoritos', on_delete=models.CASCADE)
    entrada = models.ForeignKey(
        Entrada, related_name='entradas_favoritas', on_delete=models.CASCADE)

    objects = FovoritosManager()

    class Meta:
        unique_together = ('user', 'entrada')
        verbose_name = ("Favoritos")
        verbose_name_plural = ("Favoritos")

    def __str__(self):
        return self.entrada.titulo
