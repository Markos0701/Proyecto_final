
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns=[

  path("Principal_turnos/",Principal_turnos,name="Principal_turnos"),
  path("Agenda_turnos/",Agenda_turnos,name="Agenda_turnos")
   

]