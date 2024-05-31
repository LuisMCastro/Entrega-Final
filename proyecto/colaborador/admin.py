from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Colaboradores e Imagenes"
admin.site.register(models.Colaborador)


class ImagenAdmin(admin.ModelAdmin):
    list_display = (
        "colaborador",
        "imagen",
        "titulo",
        "descripcion",
        "fecha_subida",
    )
    list_display_links = ("colaborador",)
    list_filter = ("colaborador",)
    date_hierarchy = "fecha_subida"


admin.site.register(models.Imagen, ImagenAdmin)
