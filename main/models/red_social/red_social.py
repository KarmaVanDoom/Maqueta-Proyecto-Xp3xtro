from django.db import models

class RedSocial(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.URLField(max_length=300)
    icono_class = models.CharField(max_length=100, help_text="Ej: fa-brands fa-youtube")
    handle = models.CharField(max_length=100, help_text="Ej: @SP3XTR0BEATS")
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.nombre
