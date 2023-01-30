from django.db import models
from ckeditor.fields import RichTextField,CKEditorWidget

# Create your models here.

class Mensaje(models.Model):
    emisor= models.CharField(max_length=150)
    receptor= models.CharField(max_length=50)
    cuerpo= RichTextField(blank=True,null=False)
    status= models.CharField(max_length=50)
    fecha_de_envio= models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.emisor} - {self.receptor}"