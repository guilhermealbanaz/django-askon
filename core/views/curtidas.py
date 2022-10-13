from rest_framework.viewsets import ModelViewSet
from core.serializers import CurtidasSerializer
from core.models import Curtidas

class CurtidasViewSet(ModelViewSet):
    queryset = Curtidas.objects.all()
    serializer_class = CurtidasSerializer