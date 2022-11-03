from rest_framework.serializers import ModelSerializer

from core.models import Comentario


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


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
