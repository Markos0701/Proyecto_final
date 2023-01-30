from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from django.forms.widgets import Widget, Select, MultiWidget
from django.utils.safestring import mark_safe


#===> Formulario de turnos 

class TrunosForm(forms.Form):
    
    hora_Turno= forms.TimeField(label="hora_Turno:")
    Barbero= forms.CharField(label="Barbero:",max_length=50)
    Cliente= forms.CharField(label="Cliente:",max_length=50)
    fecha_turno= forms.DateField(label="fecha_turno:",widget=forms.SelectDateWidget(years=range(1940, 2030)))
#   fecha_registro= forms.DateField(label="fecha_registro:",widget=forms.SelectDateWidget(years=range(1940, 2030)))

    """
        Codigo_Turno= models.CharField(max_length=50)
        Barbero= models.CharField(max_length=50)
        Cliente= models.CharField(max_length=50)
        fecha_turno= models.DateField(null=True, blank=True)
        fecha_registro= models.DateField(null=True, blank=True)
    
    """
   