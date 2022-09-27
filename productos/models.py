from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
