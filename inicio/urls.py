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
    path('avatar/', AgregarAvatar),
    path('verpost/', verpost),
   
    path('home/', home),
    path('login/', login_request),
    #path('UserPwd/', userForm),
    path('CvSesar/', CvSesar),
    path('CvPeralta/', CvPeralta),
    path('', homelg),
    path('newpost/', newpost),
    path('logout/', LogoutView.as_view(template_name = 'homelg.html'), name="Logout" ),
    path('home/<name>', home),
]