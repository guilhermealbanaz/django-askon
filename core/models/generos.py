from django.db import models

class Generos(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao.capitalize()