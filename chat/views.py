from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.template import Template, Context
from django.template import loader
from django.template import RequestContext
#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.decorators import login_required
from AppMiembro.views import *
from datetime import datetime,date

from .models import *

# para revisar 

from django.shortcuts import render, redirect
from chat.models import Room,Mensaje
from django.http import HttpResponse, JsonResponse

# Create your views here.

def Chat_soporte(request):
    return render(request,"Home_chat.html",{"mensaje":"Hola"},)


def home(request):
    return render(request, 'Inicio_Chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Mensaje.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Mensaje.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

   #Para el HTML que abra una nueva ventana 
   # 
   #  <a href="https://www.w3schools.com" target="_blank">Visit W3Schools</a>