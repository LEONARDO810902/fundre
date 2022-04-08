# librerias de python
from datetime import timedelta, datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from django.template.defaultfilters import slugify

# terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

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
    carousel = models.BooleanField(default=False)
    # para las paginas de url automaticas
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntradaManager()

    class Meta:
        verbose_name = ('Entrada')
        verbose_name_plural = ('Entradas')

    def __str__(self):
        return self.titulo + ' - ' + str(self.in_home) + ' - ' + str(self.portada) + ' - ' + str(self.publicar)


# procedimiento para crear la urls automaticas para CEO de la pagina


    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.titulo, str(seconds))

        self.slug = slugify(slug_unique)

        super(Entrada, self).save(*args, **kwargs)


def optimizar_imagen(sender, instance, **kwargs):

    if instance.image:
        image = Image.open(instance.image.path)
        image.save(instance.image.path, quality=20, optimize=True)


post_save.connect(optimizar_imagen, sender=Entrada)
