from rest_framework.viewsets import ModelViewSet
from core.serializers import UsuarioSerializer, UsuarioPostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Usuario


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == "create":
            return UsuarioPostSerializer
        
        return UsuarioSerializer
