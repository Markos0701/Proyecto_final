# importaciones django
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

from datetime import datetime,date

#import datetime
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.mixins import LoginRequieredMixin

# Importaciones dentro del proyecto

from .forms import *
from .models import *
from AppMiembro.views import obtenerAvatar

# PAGINA DE INICIO 

def Principal_turnos(request):
    teste={"Hola":"Markos"}
    template2= loader.get_template("principal.html")
    documento2= template2.render(teste)
    turnos= Turnos.objects.all() 
    #return HttpResponse(documento2)
    return render(request,"Home_turnos.html",{"mensaje":"", "turnos": turnos,"avatar": obtenerAvatar(request)},)

def Agenda_turnos(request):
    if request.method=="POST":

        formulario= TrunosForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            hora_Turno=info["hora_Turno"]
            Barbero=info["Barbero"]
            Cliente=info["Cliente"]
            fecha_turno=info["fecha_turno"]
            fecha_registro= date.today()
          
            turnos= Turnos(hora_Turno=hora_Turno, Barbero=Barbero, Cliente=Cliente, fecha_turno=fecha_turno, fecha_registro=fecha_registro)
            turnos.save()
            turnos= Turnos.objects.all() 
            return render(request,"Home_turnos.html" ,{"mensaje":"Se agendó turno correctamente","turnos": turnos,"avatar": obtenerAvatar(request)})
        else:
            turnos= Turnos.objects.all() 
            return render(request,"Home_turnos.html" ,{"mensaje":"La informacion ingresada no es valida","turnos": turnos,"avatar": obtenerAvatar(request)})

        return render(request,"principal.html" ,{"mensaje":"prueba ","avatar": obtenerAvatar(request)})
        
    else:
        formulario= TrunosForm()
        turnos= Turnos.objects.all() 
        return render (request, "Turnos.html", {"form_turnos": formulario,"avatar": obtenerAvatar(request)})    
