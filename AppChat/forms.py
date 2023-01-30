from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
# importaciones de AppMiembro
from AppMiembro.models import *
from django.contrib.auth import get_user_model
from .models import Mensaje
from django.forms import ModelForm
from ckeditor.fields import RichTextField


#====================  FORMS DEL PROGRAMA ====================================



class MensajeForm(forms.Form):
   #s emisor= forms.CharField(label="Nombre:",max_length=50)
    receptor= forms.CharField(label="Para:")
    cuerpo= RichTextField()
    #forms.CharField(label="Apellido:",max_length=10000)
    #status= forms.BooleanField(label="Leido:")
    # fecha_de_envio= forms.DateField(label="fecha_ingreso:",widget=forms.SelectDateWidget(years=range(1940, 2030)))
  
    #cuerpo.widget.attrs.update(size='200')

class MsjForm(ModelForm):
    class Meta:
        model= Mensaje
        fields = ['receptor','cuerpo']

    

"""  emisor= models.CharField(max_length=50)
    receptor= models.CharField(max_length=50)
    cuerpo= models.IntegerField()
    status= models.CharField(max_length=50)
    fecha_de_envio= models.DateField(null=True, blank=True)"""