from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Resenha, Jogos, Usuario, Curtidas, Comentario, Generos

class GenerosSerializer(ModelSerializer):
    class meta:
        model = Generos
        fields = '__all__'

class ResenhaSerializer(ModelSerializer):
    class Meta:
        model = Resenha
        fields = "__all__"

class JogosSerializer(ModelSerializer):
    class Meta:
        model = Jogos
        fields = "__all__"     

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

class CurtidasSerializer(ModelSerializer):
    class Meta:
        model = Curtidas
        fields = "__all__"

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"
        depth = 1                   