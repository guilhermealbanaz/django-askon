from rest_framework.serializers import ModelSerializer, CurrentUserDefault

from core.models import Resenha
from core.serializers.usuarios import UsuarioSerializer
from core.serializers.usuarios import UsuarioNestedSerializer


class ResenhaSerializer(ModelSerializer):
    usuario = UsuarioNestedSerializer()

    class Meta:
        model = Resenha
        fields = '__all__'
        depth  = 1

class ResenhaPostSerializer(ModelSerializer):

    usuario = UsuarioSerializer(default=CurrentUserDefault())

    class Meta:
        model = Resenha
        fields = ("usuario", "titulo", "descricao", "estrela", "jogo",)

