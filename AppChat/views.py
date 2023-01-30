from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import Template, Context
from django.template import loader
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppMiembro import *

from django.contrib.auth import login, authenticate


# importaciones de AppMiembro
from AppMiembro.views import *


# Create your views here.
@login_required
def Enviar_Mensaje(request):
     
    if request.method=="POST":

        usuario = request.user
        formulario= MsjForm(request.POST)

        if formulario.is_valid():
            info=formulario.cleaned_data
            emisor=usuario.username
            receptor=info["receptor"]
            cuerpo=info["cuerpo"]
            status=False
            fecha_de_envio=date.today()
            #LOGICA PARA VALIDAR USUARIO
            if usuario !=emisor is not None:
                mensaje = Mensaje(emisor= emisor, receptor= receptor,cuerpo= cuerpo ,status= status,fecha_de_envio= fecha_de_envio)
                mensaje.save()
            else:
                return render(request,"Principal.html",{"mensaje":"ingrese otro que no sea su usario"})

            return render(request,"Principal.html" ,{"mensaje":"mensaje enviado","avatar": obtenerAvatar(request)})
        else:
            return render(request,"principal.html" ,{"mensaje":"erro al enviar elñ mensaje","avatar": obtenerAvatar(request)})

    else:
        form= MsjForm()
        User = get_user_model()
        users = User.objects.all()
        return render(request,"EnviarMsj.html", {"menasaje":f"Usuarios","users":users,"form": form ,"avatar": obtenerAvatar(request)})


#===== >Leers

@login_required
def Leer_Mensajes(request):
    user=request.user
    nombre_user=user.username
    mensajes= Mensaje.objects.filter(receptor=nombre_user)
    return render(request,"ReadMsj.html",{"mensajes":mensajes,"Usuario":nombre_user,"avatar": obtenerAvatar(request)})