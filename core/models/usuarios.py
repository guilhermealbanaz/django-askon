from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    data = models.DateField(verbose_name='data de nascimento', blank= True, null=True)
    fone = models.CharField(max_length=12, null=True)
    typeuser = models.BooleanField(default=False)
    