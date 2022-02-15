from django.conf import settings
from django.db import models

# terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# managers
from .managers import EntradaManager

# Create your models here.


class Categoria(TimeStampedModel):
    short_name = models.CharField('Nombre corto', max_length=15, unique=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    """Etiquetas de un articulo"""

    name = models.CharField('Nombre', max_length=30)

    class Meta:
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')

    def __str__(self):
        return self.name


class Entrada(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    titulo = models.CharField('Titulo', max_length=200)
    resumen = models.TextField('resumen')
    contenido = RichTextUploadingField('Contenido')
    publicar = models.BooleanField(default=False)
    image = models.ImageField('Imagen', upload_to='Entrada',)
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntradaManager()

    class Meta:
        verbose_name = ('Entrada')
        verbose_name_plural = ('Entradas')

    def __str__(self):
        return self.titulo