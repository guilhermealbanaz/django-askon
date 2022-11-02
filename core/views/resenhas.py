from rest_framework.viewsets import ModelViewSet
from core.serializers import ResenhaSerializer, ResenhaPostSerializer
from core.models import Resenha

from core.paginations import ResenhaPagination


class ResenhaViewSet(ModelViewSet):
    pagination_class = ResenhaPagination

    def get_queryset(self):
        queryset = Resenha.objects.all()
        iduser = self.request.query_params.get('iduser')
        if iduser is not None:
            queryset = queryset.filter(usuario=iduser)
        return queryset

    def get_serializer_class(self):

        if self.action == "create":
            return ResenhaPostSerializer

        return ResenhaSerializer
