from rest_framework.serializers import ModelSerializer

from core.models import Jogos

class JogosSerializer(ModelSerializer):
    class Meta:
        model = Jogos
        fields = '__all__'