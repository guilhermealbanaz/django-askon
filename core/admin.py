from django.contrib import admin

from core.models import Jogos, Usuario, Resenha, Comentario, Curtidas, Generos

admin.site.register(Jogos)
admin.site.register(Usuario)
admin.site.register(Resenha)
admin.site.register(Curtidas)
admin.site.register(Comentario)
admin.site.register(Generos)