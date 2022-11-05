from rest_framework.serializers import ModelSerializer, CurrentUserDefault, CharField, SerializerMethodField
from drf_extra_fields.fields import Base64ImageField

from core.models import Resenha, Jogos, Curtidas

from core.serializers.usuarios import UsuarioSerializer, UsuarioNestedSerializer


class ResenhaSerializer(ModelSerializer):
    usuario = UsuarioNestedSerializer()
    qtd_curtidas = SerializerMethodField()

    class Meta:
        model = Resenha
        fields = '__all__'
        depth = 1

    def get_qtd_curtidas(self, instance):
        qtd_curtidas = Curtidas.objects.filter(resenha=instance.id).count()
        return qtd_curtidas


class ResenhaPostSerializer(ModelSerializer):

    usuario = UsuarioSerializer(default=CurrentUserDefault())
    imagem_resenha = Base64ImageField()
    jogo = CharField()

    class Meta:
        model = Resenha
        fields = ("id", "usuario", "titulo", "descricao",
                  "estrela", "imagem_resenha", "jogo",)

    def create(self, validated_data):
        nome_jogo = validated_data.pop("jogo")
        jogo_get = Jogos.objects.get(nome=nome_jogo)
        resenha = Resenha.objects.create(**validated_data, jogo=jogo_get)
        resenha.save()

        return resenha
