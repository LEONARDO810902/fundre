from django.db import models

from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    email = models.EmailField('Email de contacto', blank=True, null=True)
    phone = models.CharField('Telefono', max_length=15)

    class Meta:
        verbose_name = ('Pagina Principal')
        verbose_name_plural = ('Pagina Principal')

    def __str__(self):
        return self.title


class Suscribirse(TimeStampedModel):
    email = models.EmailField()

    class Meta:
        verbose_name = ('Suscritor')
        verbose_name_plural = ('Suscritores')

    def __str__(self):
        return self.email


class Contacto(TimeStampedModel):
    full_name = models.CharField('Nombres Apellidos', max_length=60)
    email = models.EmailField()
    mensaje = models.TextField()

    class Meta:
        verbose_name = ('Contacto')
        verbose_name_plural = ('Contactos')

    def __str__(self):
        return self.full_name
