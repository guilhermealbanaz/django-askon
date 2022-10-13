from rest_framework.viewsets import ModelViewSet
from core.serializers import ResenhaSerializer
from core.models import Resenha

class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer