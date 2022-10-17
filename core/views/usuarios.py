from rest_framework.viewsets import ModelViewSet
from core.serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Usuario

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]