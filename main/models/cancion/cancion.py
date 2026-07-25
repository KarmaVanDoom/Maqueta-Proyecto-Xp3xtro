from django.db import models
from main.models.artista.artista import Artista

class Cancion(models.Model):
    titulo = models.CharField(max_length=150)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='canciones')
    spotify_url = models.CharField(max_length=500, help_text="Enlace o Iframe de Spotify")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'titulo']
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"
