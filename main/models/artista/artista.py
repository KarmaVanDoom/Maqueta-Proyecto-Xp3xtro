from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='artistas/', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return self.nombre
