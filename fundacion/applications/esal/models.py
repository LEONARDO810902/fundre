from django.conf import settings
from django.db import models

# Informacion de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from applications.esal.managers import EsalManager

# Create your models here.


class Esal(TimeStampedModel):
    titulo = models.CharField('Titulo', max_length=200)
    resumen = models.TextField('resumen')
    archivo = models.FileField(upload_to="archivos/", null=True, blank=True)
    publicar = models.BooleanField(default=False)

    objects = EsalManager()

    class Meta:
        verbose_name = ('esal')
        verbose_name_plural = ('esals')

    def __str__(self):
        return self.titulo
