
from django.contrib.auth.views import LogoutView
from .views import *
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from . import views

urlpatterns = [
    path('Chat_soporte/',Chat_soporte,name='Chat_soporte'),
    path('new', views.home, name='home'),
   # path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]