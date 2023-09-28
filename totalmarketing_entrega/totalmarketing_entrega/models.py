from django.db import models
from django.contrib.auth.models import User

class Paquete(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.usuario.username} - {self.paquete.nombre}"

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.usuario.username} - {self.paquete.nombre} - {self.fecha_compra}"
