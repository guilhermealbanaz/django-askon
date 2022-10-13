from rest_framework.viewsets import ModelViewSet
from core.serializers import JogosSerializer
from core.models import Jogos

class JogosViewSet(ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer