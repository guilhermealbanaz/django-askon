from django.db import models
from core.models import Usuario, Resenha

class Curtidas(models.Model):
    def __str__(self):
        return (f'{self.usuario} curtiu {self.resenha}')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT)
    data = models.DateTimeField()