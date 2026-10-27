from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio_publicacion = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre