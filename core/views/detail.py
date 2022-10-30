from rest_framework.viewsets import ModelViewSet
from core.serializers import UsuarioSerializer
from core.models import Usuario

class DetailViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Usuario.objects.filter(id=user.id)
        return queryset