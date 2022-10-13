from rest_framework.serializers import ModelSerializer

from core.models import Curtidas

class CurtidasSerializer(ModelSerializer):
    class meta:
        model = Curtidas
        fields = '__all__'