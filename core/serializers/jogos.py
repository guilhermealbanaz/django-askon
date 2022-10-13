from rest_framework.serializers import ModelSerializer

from core.models import Jogos

class JogosSerializer(ModelSerializer):
    class meta:
        model = Jogos
        fields = '__all__'