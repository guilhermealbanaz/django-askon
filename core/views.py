from rest_framework.viewsets import ModelViewSet

from core.models import Resenha, Usuario, Comentario, Generos, Jogos, Curtidas
from core.serializers import ResenhaSerializer, UsuarioSerializer, ComentarioSerializer, GenerosSerializer, CurtidasSerializer, JogosSerializer 

class ResenhaViewSet(ModelViewSet):
    queryset = Resenha.objects.all()
    serializer_class = ResenhaSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class GenerosViewSet(ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

class CurtidasViewSet(ModelViewSet):
    queryset = Curtidas.objects.all()
    serializer_class = CurtidasSerializer

class JogosViewSet(ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer    