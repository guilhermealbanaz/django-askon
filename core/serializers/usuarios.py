from rest_framework.serializers import ModelSerializer

from core.models import Usuario
from drf_extra_fields.fields import Base64ImageField


class UsuarioSerializer(ModelSerializer):
    imagem_perfil = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = '__all__'

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password is not None:
            instance.set_password(password)

        instance.imagem_perfil = validated_data.get(
            "imagem_perfil", instance.imagem_perfil)
        instance.username = validated_data.get("username", instance.username)

        instance.save()
        return instance


class UsuarioPostSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "email", "password",)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UsuarioNestedSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("id", "username", "email", "data", "fone",)
