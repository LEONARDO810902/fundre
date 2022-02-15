from django.contrib import admin

from .models import Categoria, Tag, Entrada

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Entrada)
