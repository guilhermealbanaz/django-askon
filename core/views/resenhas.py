from rest_framework.viewsets import ModelViewSet
from core.serializers import ResenhaSerializer, ResenhaPostSerializer
from core.models import Resenha

from core.paginations import ResenhaPagination


class ResenhaViewSet(ModelViewSet):
    pagination_class = ResenhaPagination

    def get_queryset(self):
        queryset = Resenha.objects.all()
        usuario = self.request.query_params.get('usuario')
        if usuario is not None:
            queryset = queryset.filter(usuario=usuario)
        return queryset

    def get_serializer_class(self):

        if self.action == "create":
            return ResenhaPostSerializer

        return ResenhaSerializer


class MinhasResenhasViewSet(ModelViewSet):
    pagination_class = ResenhaPagination
    serializer_class = ResenhaSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Resenha.objects.filter(usuario=usuario.id)
