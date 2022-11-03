from rest_framework.serializers import ModelSerializer, CurrentUserDefault, CharField
from drf_extra_fields.fields import Base64ImageField

from core.models import Resenha, Jogos

from core.serializers.usuarios import UsuarioSerializer, UsuarioNestedSerializer


class ResenhaSerializer(ModelSerializer):
    usuario = UsuarioNestedSerializer()

    class Meta:
        model = Resenha
        fields = '__all__'
        depth = 1


class ResenhaPostSerializer(ModelSerializer):

    usuario = UsuarioSerializer(default=CurrentUserDefault())
    imagem_resenha = Base64ImageField()
    jogo = CharField()

    class Meta:
        model = Resenha
        fields = ("usuario", "titulo", "descricao",
                  "estrela", "imagem_resenha", "jogo",)

    def create(self, validated_data):
        nome_jogo = validated_data.pop("jogo")
        jogo_get = Jogos.objects.get(nome=nome_jogo)
        resenha = Resenha.objects.create(**validated_data, jogo=jogo_get)
        resenha.save()

        return resenha
