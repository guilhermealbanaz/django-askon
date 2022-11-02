from rest_framework.viewsets import ModelViewSet
from core.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Usuario


class MeuUsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Usuario.objects.filter(id=usuario.id)
