from django.urls import path
from inicio.views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
   
    #path('buscar_user/', buscar_user),
    path('registro/', registro),
    path('developers/', experiencia),
    path('perfil/',perfil),
    path('actualizar datos/', actualizar),
    path('foto/', fotoPerfil),
    #path('login/', login),
    path('', home),
    path('login/', login_request),
    #path('perfil/editarPerfil/', actualizar),
    
  
]