from django.conf import settings
from django.db import models

# Informacion de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from applications.esal.managers import EsalManager

# Create your models here.


class Esal(TimeStampedModel):

    VIGENCIA_CHOICES = (
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026')
    )

    titulo = models.CharField('Titulo', max_length=200)
    resumen = models.TextField('resumen')
    archivo = models.FileField(
        upload_to="archivos/esal/%Y/%m/%d", null=True, blank=True)
    vigencia = models.CharField(
        max_length=4, choices=VIGENCIA_CHOICES)
    publicar = models.BooleanField(default=False)

    objects = EsalManager()

    class Meta:
        verbose_name = ('esal')
        verbose_name_plural = ('esals')

    def __str__(self):
        return self.titulo
