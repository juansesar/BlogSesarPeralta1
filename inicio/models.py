from django.db import models
from django.contrib.auth.models import User


#class Datos_personales(models.Model):
#    usuario = models.EmailField()
#    contraseña = models.IntegerField()
#    def __str__(self):
#        return self.usuario

#class user(models.Model):
#    usern = models.CharField(max_length= 40)
#    first_name = models.CharField(max_length= 40)
#    last_name = models.CharField(max_length= 40)
    

class Avatar(models.Model):
    image = models.ImageField(upload_to='avatar', null = True, blank = True)

class imagenes(models.Model):
    image = models.ImageField(upload_to='imagenes', null = True, blank = True)

class Posteo(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    fecha = models.DateField()
    image = models.ImageField(upload_to='imagenes', null = True, blank = True,)