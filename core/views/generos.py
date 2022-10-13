from rest_framework.viewsets import ModelViewSet
from core.models import Generos
from core.serializers import GenerosSerializer


class GenerosViewSet(ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer