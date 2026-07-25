from django.contrib import admin
from main.models import Artista, Cancion, RedSocial

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    list_editable = ('orden',)
    search_fields = ('nombre',)

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'orden')
    list_editable = ('orden',)
    list_filter = ('artista',)
    search_fields = ('titulo', 'artista__nombre')

@admin.register(RedSocial)
class RedSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'handle', 'url', 'orden')
    list_editable = ('orden',)
    search_fields = ('nombre', 'handle')
