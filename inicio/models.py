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
    

#class Avatar(models.Model):
#    #vinculo con el usuario
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    #subcarpeta Avatares de media
#    image = models.ImageField(upload_to='avatares', null = True, blank = True)