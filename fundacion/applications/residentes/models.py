from datetime import date
from django.db import models
from django.db.models.signals import post_save

# APPS DE TERCEROS
from PIL import Image

from model_utils.models import TimeStampedModel

# Create your models here.


class Residente(TimeStampedModel):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=20)
    foto = models.ImageField('Foto', upload_to='Residentes/foto/%Y/%m/%d')
    fecha_nacimiento = models.DateField()
    eps = models.CharField(max_length=30)
    fecha_ingreso = models.DateField(default=date.today)
    fecha_salida = models.DateField(blank=True)

    class Meta:
        verbose_name = ('Residente')
        verbose_name_plural = ('Residentes')

    def __str__(self):
        return self.cedula + ' ' + self.nombre + ' ' + self.apellidos


class FamiliaresResidente(TimeStampedModel):
    cedula_residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

    class Meta:
        verbose_name = ('FamiliaresResidente')
        verbose_name_plural = ('FamiliaresResidentes')

    def __str__(self):
        return self.cedula_residente + ' ' + self.nombre + ' ' + self.apellidos


def optimizar_foto(sender, instance, **kwargs):
    if instance.foto:
        foto = Image.open(instance.foto.path)
        foto.save(instance.foto.path, quality=20, optimize=True)


post_save.connect(optimizar_foto, sender=Residente)
