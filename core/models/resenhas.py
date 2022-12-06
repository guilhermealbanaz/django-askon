from django.db import models
from core.models import Jogos, Usuario
from datetime import datetime


class Resenha(models.Model):
    imagem_resenha = models.ImageField(
        upload_to="askon/resenhas", blank=True, null=True)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(
        max_length=5000, verbose_name='descricao da resenha')
    data = models.DateTimeField(
        default=datetime.now, verbose_name='data da publicacao')
    links = models.CharField(max_length=500, null=True, blank=True)
    jogo = models.ForeignKey(Jogos, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nota_cenario = models.IntegerField(default=0)
    nota_grafico = models.IntegerField(default=0)
    nota_audio = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo
