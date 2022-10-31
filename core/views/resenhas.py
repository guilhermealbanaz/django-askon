from rest_framework.viewsets import ModelViewSet
from core.serializers import ResenhaSerializer, ResenhaPostSerializer
from core.models import Resenha

class ResenhaViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = Resenha.objects.all()
        iduser = self.request.query_params.get('iduser')
        if iduser is not None:
            queryset = queryset.filter(usuario = iduser)
        return queryset

    def get_serializerclass(self, request):
        
        if self.action == "create":
            return ResenhaPostSerializer
        
        return ResenhaSerializer
        