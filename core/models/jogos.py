from django.db import models
from core.models import Generos

class Jogos(models.Model):
    imagem = models.ImageField(upload_to="askon/jogos/", blank=True, null=True)
    data = models.DateField()
    idade = models.IntegerField()
    nome = models.CharField(max_length=200)
    genero = models.ManyToManyField(Generos, related_name='generos')

    def __str__(self):
        return self.nome
