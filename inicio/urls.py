from django.urls import path
from inicio.views import *
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
   
    #path('buscar_user/', buscar_user),
    path('registro/', registro),
    path('developers/', experiencia),
    path('perfil/',perfil),
    path('actualizar/', actualizar),
    path('avatar/', AgregarAvatar),
    #path('verpost/', verpost),
    path('delete/', delete),
    path('home/', home),
    path('login/', login_request),
    #path('UserPwd/', userForm),
    path('CvSesar/', CvSesar),
    path('CvPeralta/', CvPeralta),
    path('', homelg),
    path('newpost/', newpost),
    path('logout/', LogoutView.as_view(template_name = 'homelg.html'), name="Logout" ),
    path('home/<name>', home),
    #path('verpost', verpost),
    path('cambiarContraseña', cambiarContraseña),
    path('deletePost/<p_id>', deletePost),
    path('actualizarpost/<p_id>', actualizarpost),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)