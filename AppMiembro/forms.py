from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

#====================  FORMS DEL PROGRAMA ====================================

#===> Formulario Colaboradores

class ColaboradorForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    apellido= forms.CharField(label="Apellido:",max_length=50)
    dni= forms.IntegerField(label="DNI:",)
    cargo= forms.CharField(label="cargo:",max_length=50)
    fecha_ingreso= forms.DateField(label="fecha_ingreso:",widget=forms.SelectDateWidget(years=range(1940, 2030)))

#===> Formulario Clientes

class ClienteForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    apellido= forms.CharField(label="Apellido:",max_length=50)
    dni= forms.IntegerField(label="DNI:",)
    asignado_a = forms.CharField(label="Barbero_asignado:",max_length=50)
    fecha_registro= forms.DateField(label="fecha_registro:",widget=forms.SelectDateWidget(years=range(1940, 2030)))

#===> Formulario Productos

class ProductoForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    marca= forms.CharField(label="marca:",max_length=50)
    codigo= forms.IntegerField(label="codigo:",)
    cantidad= forms.CharField(label="cantidad:",max_length=50)

#===> Formulario Ventas

class VentasForm(forms.Form):
    barbero= forms.CharField(label="barbero:",max_length=50)
    servicio= forms.CharField(label="servicio:",max_length=50)
    servicio_cant= forms.IntegerField(label="servicio_cant:")
    producto= forms.CharField(label="producto:",max_length=50)
    producto_cant= forms.IntegerField(label="producto_cant:")
#    fecha_registro= forms.DateField(label="fecha_registro:",widget=forms.SelectDateWidget(years=range(1940, 2030)))


#==================== GESTION DE USUARIOS ====================================


#===> Formulario Registro de Usuarios

# ===(1) 

class RegistroUsuarioForm(UserCreationForm):

    firstname= forms.CharField(label="firstname",max_length=50)
    lastname= forms.CharField(label="lastname",max_length=50)
    email= forms.EmailField(label="email")
    password1= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="confirmar Contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        model= User
        fields= ["username","firstname","lastname","email", "password1","password2"]
        help_texts= {k:"" for k in fields}

# ===(2) 

class UserEditForm(UserCreationForm):

    # Obligatorios

    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

#===> Formularios para avatars y contenido

# ===(1) 
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

