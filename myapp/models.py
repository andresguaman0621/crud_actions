from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicacion = models.DateField()

    def __str__(self):
        return str(self.titulo)
