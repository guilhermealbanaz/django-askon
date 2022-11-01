from rest_framework.serializers import ModelSerializer

from core.models import Jogos
from core.serializers.generos import GenerosSerializer

class JogosSerializer(ModelSerializer):
    genero = GenerosSerializer(many=True)

    class Meta:
        model = Jogos
        fields = '__all__'