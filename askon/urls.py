from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from core.views import DetailViewSet, ResenhaViewSet, UsuarioViewSet, JogosViewSet, GenerosViewSet, CurtidasViewSet, ComentarioViewSet, MeuUsuarioViewSet, MinhasResenhasViewSet

router = DefaultRouter()
router.register(r"Resenhas", ResenhaViewSet, basename='resenhaid')
router.register(r"usuarios", UsuarioViewSet)
router.register(r"jogos", JogosViewSet)
router.register(r"generos", GenerosViewSet)
router.register(r"curtidas", CurtidasViewSet)
router.register(r"comentario", ComentarioViewSet)
router.register(r"details", DetailViewSet, basename='Usuariologado')
router.register(r"meu_usuario", MeuUsuarioViewSet, basename='meu_usuario')
router.register(r"minhas_resenhas", MinhasResenhasViewSet,
                basename='minhas_resenhas')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
