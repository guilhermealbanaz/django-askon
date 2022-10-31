from rest_framework.serializers import ModelSerializer

from core.models import Resenha
from core.serializers.usuarios import UsuarioNestedSerializer


class ResenhaSerializer(ModelSerializer):
    usuario = UsuarioNestedSerializer()

    class Meta:
        model = Resenha
        fields = '__all__'
        depth  = 1
