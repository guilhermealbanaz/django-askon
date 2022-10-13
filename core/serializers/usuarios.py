from rest_framework.serializers import ModelSerializer

from core.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class meta:
        model = Usuario
        fields = '__all__'