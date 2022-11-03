from rest_framework.viewsets import ModelViewSet
from core.serializers import CurtidasSerializer
from core.models import Curtidas, Resenha


class CurtidasViewSet(ModelViewSet):
    serializer_class = CurtidasSerializer

    def get_queryset(self):
        usuario = self.request.user
        id_resenha = self.request.query_params.get("id_resenha")

        return Curtidas.objects.filter(usuario=usuario, resenha=id_resenha)
