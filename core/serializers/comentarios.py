from rest_framework.serializers import ModelSerializer

from core.models import Comentario

from core.serializers.usuarios import UsuarioNestedSerializer


class ComentarioSerializer(ModelSerializer):
    usuario = UsuarioNestedSerializer()

    class Meta:
        model = Comentario
        fields = ("comentario", "data", "usuario",)


class ComentarioPostSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("comentario", "resenha",)

    def create(self, validated_data):
        usuario = self.context["request"].user

        comentario = Comentario.objects.create(
            **validated_data, usuario=usuario)

        comentario.save()
        return comentario
