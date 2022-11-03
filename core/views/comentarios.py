from rest_framework.viewsets import ModelViewSet
from core.serializers import ComentarioSerializer, ComentarioPostSerializer
from core.models import Comentario


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ComentarioPostSerializer
        return ComentarioSerializer

    def get_queryset(self):
        id_resenha = self.request.query_params.get("id_resenha")

        return Comentario.objects.filter(resenha=id_resenha).order_by("data")
