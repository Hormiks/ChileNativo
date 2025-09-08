from django.contrib import admin
from .models import Especie, Noticia, Faq

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ("nombre_comun", "nombre_cientifico", "tipo", "estado_conservacion")
    search_fields = ("nombre_comun", "nombre_cientifico")
    list_filter = ("tipo", "estado_conservacion")

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_publicacion")
    search_fields = ("titulo",)

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("pregunta",)
    search_fields = ("pregunta",)
