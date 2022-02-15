from django.db import models


class EntradaManager(models.Manager):

    def entrada_en_portada(self):
        return self.filter(
            publicar=True,
            portada=True,
        ).order_by('-created').first()

    def entrada_en_home(self):
        return self.filter(
            publicar=True,
            in_home=True,
        ).order_by('-created')[:4]

    def entrada_en_recientes(self):
        return self.filter(
            publicar=True,
        ).order_by('-created')[:6]
