
from django.contrib.auth.views import LogoutView
from django.urls import path
from AppChat.views import *



urlpatterns=[

  #path("Home_chat/",Home_chat,name=Home_chat),
  path("Enviar_Mensaje/",Enviar_Mensaje,name="Enviar_Mensaje"),
  path("Leer_Mensajes/",Leer_Mensajes,name="Leer_Mensajes"),
   

]