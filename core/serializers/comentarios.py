from rest_framework.serializers import ModelSerializer

from core.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class meta:
        model = Comentario
        fields = '__all__'