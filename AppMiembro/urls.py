from django.urls import path , include
from .views import *
from django.contrib.auth.views import LogoutView

from Turnos.views import *

urlpatterns=[
    
    #sitios Para Eliminar 
    #path("sitio/",Sitio_web,name="Sitio_web"),

    # ==== > URL pirncipales

    path("",Principal,name="Sitio_principal"),
    path("Sitio_principal/",Principal,name="Sitio_principal"),

    # ==== > URL Colaboradores
    
    path("Colaboradores_site/",Colaboradores_site,name="Colaboradores_site"),
    path("Colaborador_site/",Colaborador_site,name="Colaborador_site"),
    path("ingreso_colaborador/",Ing_colaborador,name="colaborado"),

    # ==== > URL Productos

    path("Producto_site/",Producto_site,name="Producto_site"),
    path("ingreso_producto/",Ing_producto,name="ing_producto"),
    path("Producto_Busqueda/",Producto_Busqueda,name="Producto_Busqueda"),

    # ==== > URL Clientes

    path("Ingreso_clientes/",Clientes_site,name="Clientes_site"),
    path("leer_clientes/",leerclientes,name="leer_clientes"),
    path("eliminar_cliente/<id>",eliminar_cliente,name="eliminar_cliente"),
    path("editarCliente/<id>",editarCliente,name="editarCliente"),

    # ==== > URL Gestion de Usuarios.

    path("register/",register,name="register"),
    path("Logeando/",Logeando,name="Logeando"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("editarperfil/",editarperfil, name= "editarperfil"),
    path("agregarAvatar/",agregarAvatar, name= "agregarAvatar"),

    # ====> Ventas

    path("Ventas_Site/",Ventas_Site,name="Ventas_Site"),  

    path("About/",About,name="About"),  

    # ==== > URL Para depurar

    path("Familiar_site/",Familiar_site,name="Familiar_site"),
    path("miembro/",familiar,name="familiar"),

    path("Turnos/miembro/",Principal_turnos,name="Principal_turnos"),
    

    



]