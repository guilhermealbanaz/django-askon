from rest_framework.viewsets import ModelViewSet
from core.serializers import ComentarioSerializer
from core.models import Comentario

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer