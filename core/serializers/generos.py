from rest_framework.serializers import ModelSerializer

from core.models import Generos

class GenerosSerializer(ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'