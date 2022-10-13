from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from core.models import Jogos, Usuario, Resenha, Comentario, Curtidas, Generos

admin.site.register(Jogos)
admin.site.register(Resenha)
admin.site.register(Curtidas)
admin.site.register(Comentario)
admin.site.register(Generos)

class UsuarioAdmin(UserAdmin):
    fieldsets = (
            (None, {"fields": ("username", "password")}),
            (_("Personal info"), {"fields": ("first_name", "last_name", "email", "typeuser", "fone", "data")}),
            (
                _("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        )

admin.site.register(Usuario, UsuarioAdmin)