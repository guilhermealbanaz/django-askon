from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from core.models import Resenha, Usuario, Comentario, Generos, Jogos, Curtidas
from core.serializers import ResenhaSerializer, UsuarioSerializer, ComentarioSerializer, GenerosSerializer, CurtidasSerializer, JogosSerializer 

class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer
    # permission_classes = [IsAuthenticated]
    

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # permission_classes = [IsAuthenticated]

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    # serializer_class = ComentarioSerializer

class GenerosViewSet(ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer
    # permission_classes = [IsAuthenticated]

class CurtidasViewSet(ModelViewSet):
    queryset = Curtidas.objects.all()
    serializer_class = CurtidasSerializer
    # permission_classes = [IsAuthenticated]

class JogosViewSet(ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer
    # permission_classes = [IsAuthenticated]    