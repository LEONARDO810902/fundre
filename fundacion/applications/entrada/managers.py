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

    def entrada_corousel_home(self):
        return self.filter(
            publicar=True,
            carousel=True,
        ).order_by('-created')

    def entrada_en_recientes(self):
        return self.filter(
            publicar=True,
        ).order_by('-created')[:4]

    def Buscar_entradas(self, buscarentrada, categoria):
        # procedimiento para buscar las entradas  por palabra clave
        if len(categoria) > 0:
            return self.filter(
                categoria__short_name=categoria,
                titulo__icontains=buscarentrada,
                publicar=True,
            ).order_by('-created')
        else:
            return self.filter(
                titulo__icontains=buscarentrada,
                publicar=True,
            ).order_by('-created')
