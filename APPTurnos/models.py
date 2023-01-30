
from django.db import models

# Create your models here.

class Turnos(models.Model):
    hora_Turno= models.CharField(max_length=50)
    Barbero= models.CharField(max_length=50)
    Cliente= models.CharField(max_length=50)
    fecha_turno= models.DateField(null=True, blank=True)
    fecha_registro= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.Barbero} - {self.Codigo_Turno}"

