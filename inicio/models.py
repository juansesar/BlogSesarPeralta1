from django.db import models
from django.contrib.auth.models import User


class Datos_personales(models.Model):
    usuario = models.EmailField()
    contraseña = models.IntegerField()
    def __str__(self):
        return self.usuario

class user(models.Model):
    username = models.CharField(max_length= 40)
    first_name = models.CharField(max_length= 40)
    last_name = models.CharField(max_length= 40)
    

class avatar(models.Model):
    image = models.ImageField(upload_to='avatar', null = True, blank = True)