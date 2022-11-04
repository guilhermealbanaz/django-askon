from rest_framework.viewsets import ModelViewSet
from core.serializers import ResenhaSerializer, ResenhaPostSerializer
from core.models import Resenha, Curtidas
from datetime import datetime
from django.http import HttpResponse

from rest_framework.decorators import action

from core.paginations import ResenhaPagination, ResenhaPerfilPagination


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

    @action(detail=True, methods=['get'])
    def curtir(self, request, pk):
        usuario = self.request.user
        resenha = Resenha.objects.get(id=pk)

        try:
            curtida = Curtidas.objects.get(resenha=resenha, usuario=usuario)
        except Curtidas.DoesNotExist:
            curtida = None

        if curtida is None:
            curtida = Curtidas.objects.create(
                resenha=resenha, usuario=usuario, data=datetime.now())
            curtida.save()
            return HttpResponse(content=f'{usuario.username} curtiu a resenha {resenha.titulo}')
        else:
            curtida.delete()
            return HttpResponse(content=f'{usuario.username} deixou de curtir a resenha {resenha.titulo}')


class MinhasResenhasViewSet(ModelViewSet):
    pagination_class = ResenhaPerfilPagination
    serializer_class = ResenhaSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Resenha.objects.filter(usuario=usuario.id)


class MinhasResenhasViewSet(ModelViewSet):
    pagination_class = ResenhaPerfilPagination
    serializer_class = ResenhaSerializer

    def get_queryset(self):
        id_usuario = self.request.query_params.get("id_usuario")

        return Resenha.objects.filter(usuario=id_usuario)
