from django.db import models

class Jogos(models.Model):
    def __str__(self):
        return self.nome
    data = models.DateField()
    idade = models.IntegerField()
    nome = models.CharField(max_length=200)

class Usuario(models.Model):
    def __str__(self):
        return self.nome
    senha = models.CharField(max_length=45)
    data = models.DateField(verbose_name='data de nascimento')
    email = models.CharField(max_length=120)
    fone = models.CharField(max_length=12)
    typeuser = models.BooleanField(default=False)
    nome = models.CharField(max_length=50)


class Resenha(models.Model):
    def __str__(self):
        return self.titulo 
    titulo = models.CharField(max_length=100)    
    descricao = models.CharField(max_length=5000, verbose_name='descrição da resenha')
    data = models.DateTimeField(verbose_name='data da publicação')
    links = models.CharField(max_length=500)
    jogo = models.ForeignKey(Jogos, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Curtidas(models.Model):
    def __str__(self):
        return (f'{self.usuario} curtiu {self.resenha}')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT)
    data = models.DateTimeField()

class Comentario(models.Model):
    def __str__(self):
        return (f'{self.usuario} comentou em {self.resenha}')
    comentario = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    resenha = models.ForeignKey(Resenha, on_delete=models.PROTECT)
    data = models.DateTimeField()



    
