from django.db import models


class EsalManager(models.Manager):

    def Listado_esal_portada(self):
        return self.filter(
            publicar=True,
            vigencia=2022,
        ).order_by('-created')
