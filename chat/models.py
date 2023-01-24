from django.db import models
from datetime import datetime


class Room(models.Model):
    Nombre= models.CharField(max_length=50)

class Mensaje(models.Model):
    Valor= models.CharField(max_length=10000)
    date= models.DateTimeField(default=datetime.now, blank=True)
    User= models.CharField(max_length=100)
    room= models.CharField(max_length=100)


