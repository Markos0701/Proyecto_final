from django.db import models
from datetime import*
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class Miembro(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    edad= models.IntegerField()
    afinidad= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.afinidad}"

class Cliente(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    asignado_a= models.CharField(max_length=50)
    fecha_registro= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.asignado_a}"

class Colaborador(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    cargo= models.CharField(max_length=50)
    fecha_ingreso= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.cargo}"
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    marca= models.CharField(max_length=50)
    codigo= models.IntegerField()
    cantidad= models.IntegerField()
    fecha_registro= models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.marca}"

class Ventas(models.Model):
    barbero= models.CharField(max_length=50)
    servicio= models.CharField(max_length=50)
    servicio_cant= models.IntegerField()
    producto= models.CharField(max_length=50)
    producto_cant= models.IntegerField()
    fecha_registro= models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.barbero} - {self.fecha_registro}"

    

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    creador= models.CharField(('titulo'),max_length=100)
    titulo= models.CharField(('titulo'),max_length=100)
    contenido=RichTextUploadingField(blank=True,null=False)
    fecha_de_posteo= models.DateTimeField('fecha_de_posteo')


class Posteo(models.Model):
 
    titulo= models.CharField(('titulo'),max_length=100)
    contenido=RichTextUploadingField(blank=True,null=False)
    fecha_de_posteo= models.DateTimeField('fecha_de_posteo')
    slug = models.SlugField(default='',blank=True)

    def save(self):
        self.slug= slugify(self.titulo)

    def __str__(self) -> str:
        return '%s' % self.titulo
  