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

#Importaciones no utilizadas

from datetime import datetime,date
#import datetime
#from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.mixins import LoginRequieredMixin

# Importaciones dentro del proyecto

from .forms import *
from .models import *

#_______________________ Funciones o vistas ____________________________________

# FUNCION CARGA DEL AVATAR A LAS URL
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar= "/media/avatars/Avatar1.png"
    return avatar

# VIEWS DEL PROGRAMA.

# PAGINA DE INICIO 

def Principal(request):
    teste={"Hola":"Markos"}
    template2= loader.get_template("principal.html")
    documento2= template2.render(teste)
    return render(request,"Principal.html",{"mensaje":"Contenido"})

    
# FUNCIONES DE BASE DE DATOS


# ===> FUNCIONES DE COLABORADORES

def Colaboradores_site(request):
    """ teste={"Hola":"Markos"}
    template= loader.get_template("Colaborador.html")
    documento= template.render(teste)
    return HttpResponse(documento)"""

    colaborador= Colaborador.objects.all()
    return render (request,"Colaborador.html",{"colaboradores": colaborador, "avatar": obtenerAvatar(request)})

@login_required
def Ing_colaborador(request):

    colaborador_nuevo= Colaborador(nombre="enmanuel", apellido= "Mavarez",dni=95711470, cargo= "programador", fecha_ingreso= datetime.date(2014, 12, 25))
    colaborador_nuevo.save()
    cadena_texto= f"colaborador Guardado: Nombre: {colaborador_nuevo.nombre}  ,__Apellido: {colaborador_nuevo.apellido}  ,__dni: {colaborador_nuevo.dni}  ,__cargo: {colaborador_nuevo.cargo}  ,__fecha_ingreso: {colaborador_nuevo.fecha_ingreso}"
    return HttpResponse(cadena_texto)

@login_required
def Colaborador_site(request):
    if request.method=="POST":
        formulario= ColaboradorForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            dni=info["dni"]
            cargo=info["cargo"]
            fecha_ingreso=info["fecha_ingreso"]
            colaborador= Colaborador(nombre= nombre, apellido= apellido,dni=dni,cargo= cargo,fecha_ingreso= fecha_ingreso)
            colaborador.save()
            return render(request,"Principal.html" ,{"mensaje":"colaborador editado correctamente","colaboradores": colaborador,"avatar": obtenerAvatar(request)})
        else:
            return render(request,"principal.html" ,{"mensaje":"La informacion del colaborador ingresada no es valida","colaboradores": colaborador,"avatar": obtenerAvatar(request)})

    else:
        formulario= ColaboradorForm()
        colaborador= Colaborador.objects.all()
        return render (request, "Colaborador_form.html", {"form_colaborador": formulario,"colaboradores": colaborador,"avatar": obtenerAvatar(request)})    


# ===> VIEWS DE VENTAS

def Ventas_Site(request):
    if request.method=="POST":
        formulario= VentasForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            barbero=info["barbero"]
            servicio=info["servicio"]
            servicio_cant=info["servicio_cant"]
            producto=info["producto"]
            producto_cant=info["producto_cant"]
            fecha_registro= date.today()
          #  cliente = Cliente(nombre= barbero, servicio= servicio,servicio_cant= servicio_cant ,producto= producto,producto_cant= producto_cant)
            ventas= Ventas(barbero=barbero, servicio=servicio, servicio_cant=servicio_cant, producto=producto, producto_cant=producto_cant,fecha_registro= fecha_registro )
          # cliente.save()
            ventas.save()

            return render(request,"Principal.html" ,{"mensaje":"Tu registro se realizo de manera correctamente","avatar": obtenerAvatar(request)})
        else:
            return render(request,"principal.html" ,{"mensaje":"La informacion ingresada no es valida","avatar": obtenerAvatar(request)})

        return render(request,"principal.html" ,{"mensaje":"prueba ","avatar": obtenerAvatar(request)})
    else:
        formulario= VentasForm()
        ventas= Ventas.objects.all() 
        return render (request, "Ventas.html", {"form_ventas": formulario, "ventas": ventas,"avatar": obtenerAvatar(request)})    


# ===> FUNCIONES PARA CLASIFICAR

def Sitio_web(request):

    diccionario={"nombre":"Markos","apellido":"Mavarez","edad":str(28),"lista_de_notas":[10,9,5,7,8]}
    template= loader.get_template("template1.html")
    documento= template.render(diccionario)
    return HttpResponse(documento)



# Ingresos de datos a DB 
@login_required
def familiar(request):

    familiar_nuevo= Miembro(nombre="enmanuel", apellido= "Mavarez",edad=30, afinidad= "hermano", fecha_nacimiento= datetime.date(1995, 12, 25))
    familiar_nuevo.save()
    cadena_texto= f"Familiar Guardado: Nombre: {familiar_nuevo.nombre}  ,__Apellido: {familiar_nuevo.apellido}  ,__Edad: {familiar_nuevo.edad}  ,__afinidad: {familiar_nuevo.afinidad}  ,__fecha: {familiar_nuevo.fecha_nacimiento}"
    return HttpResponse(cadena_texto)




@login_required
def Ing_producto(request):

    producto_nuevo= Producto(nombre="Cera", marca= "barshop",codigo= 95711470, cantidad= 5, fecha_registro= datetime.date(2014, 12, 25))
    producto_nuevo.save()
    cadena_texto= f"Producto Guardado: Nombre: {producto_nuevo.nombre}  ,__Marca: {producto_nuevo.marca}  ,__dni: {producto_nuevo.codigo}  ,__cargo: {producto_nuevo.cantidad}  ,__fecha_registro: {producto_nuevo.fecha_registro}"
    return HttpResponse(cadena_texto)
    


# ingreso desde formularios

#@csrf_exempt
def Familiar_site(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        edad=request.POST["edad"]
        afinidad=request.POST["afinidad"]
        fecha_nacimiento=request.POST["fecha_nacimiento"]
        familiar_nuevo= Miembro(nombre= nombre, apellido= apellido,edad=edad, afinidad= afinidad, fecha_nacimiento= fecha_nacimiento)
        familiar_nuevo.save()
        return render(request,"Principal.html",{"mensaje":"Familiar guardado Correctamente"},)
    else:
        teste={"Hola":"Markos"}
        template= loader.get_template("familiar.html")
        documento= template.render(teste)
        return HttpResponse(documento) 


    
@login_required
def Producto_site(request):

    if request.method=="POST":
        formulario= ProductoForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info["nombre"]
            marca=info["marca"]
            codigo=info["codigo"]
            cantidad=info["cantidad"]
            producto= Producto(nombre= nombre, marca= marca,codigo=codigo ,cantidad= cantidad)
            producto.save()
            return render(request,"Principal.html" ,{"mensaje":"Producto ingresado correctamente","avatar": obtenerAvatar(request)})
        else:
            return render(request,"principal.html" ,{"mensaje":"La informacion del Producto ingresada no es valida","avatar": obtenerAvatar(request)})

    else:
        formulario= ProductoForm()

        return render (request, "Producto_form.html", {"ProductoForm": formulario, "avatar": obtenerAvatar(request)})     



# ingreso de clientes 

@login_required
# ingresos de clientes 
def Clientes_site(request):
    if request.method=="POST":
        formulario= ClienteForm(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            dni=info["dni"]
            asignado_a=info["asignado_a"]
            fecha_registro=info["fecha_registro"]
            cliente = Cliente(nombre= nombre, apellido= apellido,dni= dni ,asignado_a= asignado_a,fecha_registro= fecha_registro)
            cliente.save()
            return render(request,"Principal.html" ,{"mensaje":"Tu registro se realizo de manera correctamente","avatar": obtenerAvatar(request)})
        else:
            return render(request,"principal.html" ,{"mensaje":"La informacion ingresada no es valida","avatar": obtenerAvatar(request)})

    else:
        formulario= ClienteForm()

        #Ver clientes
        clientes= Cliente.objects.all()
        return render (request, "clientes_N.html", {"ClienteForm": formulario,"clientes": clientes, "avatar": obtenerAvatar(request)})     



@login_required
def leerclientes(request):

    clientes= Cliente.objects.all()
    return render (request,"clientes_N.html",{"clientes": clientes, "avatar": obtenerAvatar(request)})

@login_required
def eliminar_cliente(request,id):

    cliente=Cliente.objects.get(id=id)
    print(cliente)
    cliente.delete()
    clientes= Cliente.objects.all()
    return render (request, "clientes_N.html", {"clientes": clientes})     
    
    return

@login_required
def editarCliente(request,id):
    cliente= Cliente.objects.get(id=id)
    if request.method=="POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            cliente.nombre=info["nombre"]
            cliente.apellido=info["apellido"]
            cliente.dni=info["dni"]
            cliente.asignado_a=info["asignado_a"]
            cliente.fecha_registro=info["fecha_registro"]
            cliente.save()
            #Ver clientes
            formulario= ClienteForm()
            clientes= Cliente.objects.all()
            return render (request, "clientes_N.html", {"ClienteForm": formulario,"clientes": clientes})     

    else:
        formulario= ClienteForm(initial={"nombre":cliente.nombre,"apellido":cliente.apellido,"dni":cliente.dni,"asignado_a":cliente.asignado_a,"fecha_registro":cliente.fecha_registro})
        return render (request, "Cliente_editar.html", {"form":formulario ,"cliente": cliente})


# busqueda en la base de datos  /Producto_Busqueda

@login_required
def Producto_Busqueda(request):

    nombre= request.GET["PRODUCTO"]

    if nombre!="":
            productos= Producto.objects.filter(nombre=nombre)
            return render(request, "Productos_lista.html", {"productos":productos})
    else:
            return render(request, "Producto_form.html", {"mensaje":"! Ingrese una producto ¡"})



# Seccion para registrar usuarios 

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)

        if form.is_valid():
            Username= form.cleaned_data.get("username")
            form.save()
            return render(request,"Principal.html" ,{"mensaje":"Tu usuario se creo de manera correcta"})
        else:
            return render(request,"Principal.html" ,{"mensaje":"Error al registrar el usuario"})    
    else:
        form= RegistroUsuarioForm()
        return render(request, "Registro.html", {"form": form})

def Logeando(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info= form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe
            if usuario is not None:
                login(request, usuario)
                return render(request,"Principal.html",{"mensaje":f"Usuario {usu} logueado corectamente"})
            else:
                return render(request,"Principal.html",{"mensaje":"usuario y contraseña incorrectos"})
        else:
            return render(request,"Logeado.html",{"form":form})
    else:
        form=AuthenticationForm()
        return render(request, "Logeado.html",{"form":form})


#copiado de la clase de franco 

@login_required
def editarperfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()
            return render(request,"Principal.html",{"mensaje":"Usuario Editado Correctamente","avatar": obtenerAvatar(request)})
        else:
             
            form = UserEditForm(instance=usuario)
        return render(request, "Editarperfil.html", {"form": form,"mensaje":f"Error al editar usurio: {usuario.username}"})
    else:

        form = UserEditForm(instance=usuario)
        return render(request, "Editarperfil.html", {"form": form,"mensaje":f"editando usuario : {usuario.username}","avatar": obtenerAvatar(request)})


def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request,"Principal.html",{"mensaje":"Avatar agregado Correctamente","avatar": obtenerAvatar(request)})
        else:
            return render(request,"agregarAvatar.html",{"form": form,"usuario":request.user,"mensaje":"Error al agregar avatar","avatar": obtenerAvatar(request)})
    else:
        form= AvatarForm()
        return render(request, "agregarAvatar.html",{"form": form,"usuario":request.user,"mensaje":"Agrega la imagen de tu Avatar","avatar": obtenerAvatar(request)})

def About(request):
    return render(request, "About.html",{"mensaje":"Sección de Desarrolladores","avatar": obtenerAvatar(request)})