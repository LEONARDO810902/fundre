from django.db import models


class FovoritosManager(models.Manager):

    def entradas_user(self, usuario):
        return self.filter(
            entrada__publicar=True,
            user=usuario,
        ).order_by('-created')
