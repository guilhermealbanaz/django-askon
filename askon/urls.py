from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import ResenhaViewSet, UsuarioViewSet, JogosViewSet, GenerosViewSet, CurtidasViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r"Resenhas", ResenhaViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"jogos", JogosViewSet)
router.register(r"generos", GenerosViewSet)
router.register(r"curtidas", CurtidasViewSet)
router.register(r"comentario", ComentarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]