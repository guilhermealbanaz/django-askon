from django.db import models
from core.models import Usuario, Resenha

class Comentario(models.Model):
    def __str__(self):
        return (f'{self.usuario} comentou em {self.resenha}')
    comentario = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT)
    data = models.DateTimeField()