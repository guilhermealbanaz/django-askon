from django.db import models
from core.models import Usuario, Resenha
from datetime import datetime


class Comentario(models.Model):
    comentario = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT)
    data = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return (f'{self.usuario} comentou em {self.resenha}')
