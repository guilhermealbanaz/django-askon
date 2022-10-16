from django.db import models
from core.models import Jogos, Usuario

class Resenha(models.Model):
    nota_choices = (
        (1, "1 estrela"),
        (2, "2 estrelas"),
        (3, "3 estrelas"),
        (4, "4 estrelas"),
        (5, "5 estrelas"),  
    )

    estrela = models.IntegerField(null=False, choices=nota_choices) 
    titulo = models.CharField(max_length=100)    
    descricao = models.CharField(max_length=5000, verbose_name='descricao da resenha')
    data = models.DateTimeField(verbose_name='data da publicacao')
    links = models.CharField(max_length=500)
    jogo = models.ForeignKey(Jogos, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    def __str__(self):
        return self.titulo