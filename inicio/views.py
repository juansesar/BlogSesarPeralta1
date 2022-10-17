from asyncio.windows_events import NULL
from re import template
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inicio.forms import *
from inicio.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from inicio.template import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pprint
# Create your views here.
def home(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    post = Posteo.objects.all()
    
    return render(request, "home.html", {"post": post, 'avatar': avatar}) 
    
    #return render (request, "home.html")

def homelg(request):
    return render (request, "homelg.html")

def CvSesar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "CvSesar.html", {'avatar': avatar})
    

def CvPeralta(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "CvPeralta.html", {'avatar': avatar})
    

#def registro(request):
#    if request.method == "POST":
#        usuario= user(usern = request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'] )
#        usuario.save()
#        return render(request, "userForm.html")
#    return render(request, "registro.html")

#def perfil(request):
#    return render (request, "perfil.html")

def perfil(request):
    usuario = request.user
    usuario =User.objects.filter(username__icontains= usuario.username) 
    respuesta= {"usuario": usuario}
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "perfil.html", {"usuario": usuario, 'avatar': avatar})

#def perfil(request):
#    usuario = request.user
#    usuario =User.objects.filter(username__icontains= usuario.username) 
#    respuesta= {"usuario": usuario}
#    avatar = Avatar.objects.filter(user = request.user.id)
#    try:
#        avatar = avatar[0].image.url
#    except:
#        avatar = None
#    return render(request, 'perfil.html', {'avatar': avatar}, {"usuario": usuario})

def fotoPerfil(request):
    return render (request, "fotoPerfil.html")

def experiencia(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "experiencia.html", { 'avatar': avatar})
    

#def actualizar(request):
#    if request.method == 'POST':
#        formulario = UserEditForm(request.POST)
#        if formulario.is_valid():
#            informacion= formulario.cleaned_data
#            usuario= User(username = informacion['username'], email = informacion['email'], first_name = informacion['first_name'], last_name = informacion['last_name'],password= informacion['password'] )
#            usuario.save()
#            return render (request, "perfil.html")
#    else:
#        formulario = UserEditForm()
#    formulario = UserEditForm()
#    return render (request, "actualizar.html", {'formulario': formulario})
    
def registro(request):  
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render (request, "homelg.html")
        else:
            return redirect(request, "registro.html", {'form': form})  
    form = UserRegisterForm()
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "registro.html", {'form': form, 'avatar': avatar})  

#def login(request):
#    return render (request, "login.html")

def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            pwd = formulario.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)
            #return render(request, 'home.html')
            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                post= Posteo.objects.all()    
                return render(request, 'home.html', {'avatar': avatar, 'post': post})
            else:
                return render(request, "login.html", {'formulario':formulario})
        else:
            return render(request, "login.html", {'formulario':formulario})
    formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})

#@login_required
def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(id = request.user.id)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'perfil.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'avatar.html', {'form': form})           
    
#def newpost(request):
#    if request.method == 'POST':
#        formulario = Posteo(request.POST, request.FILES)
#        post= Posteo(image = formulario['imagen'], titulo= formulario['titulo'], subtitulo= formulario['subtitulo'], cuerpo= formulario['cuerpo'], fecha= formulario['fecha'])
#        post.save()
#        return render(request, "home.html", {'post':post})
#    return render(request, "newpost.html")

def newpost(request): 
    user=User.objects.get(username = request.user.username)
    if request.method == 'POST':
            post= Posteo(request.POST, request.FILES)
            #user=User.objects.get(id = request.user.id)
            post= Posteo(user=user, image = request.FILES.get("img", False) , titulo= request.POST['titulo'] , subtitulo= request.POST['subtitulo'] , cuerpo= request.POST['cuerpo'] , fecha= request.POST['fecha'])
            post.save()
            post= Posteo.objects.all()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            
            return render (request, "home.html", {'post': post, 'avatar': avatar})
    else:
            "faltan datos"
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    form =ImagenFormulario()
    return render (request, "newpost.html", {'form': form, 'avatar': avatar, 'username': user}) 
#
#def verpost(request):
#    post = Posteo.objects.get(post= request.all)
#    return render(request, "home.html", {"post": post})   
#    #return HttpResponse( {"post": post})

#def Agregarimagen(request):
#    if request.method == 'POST':
#        form = ImagenFormulario(request.POST, request.FILES)
#        print(form)
#        print(form.is_valid())
#        if form.is_valid():
#            imagen = imagenes( imagen = form.cleaned_data['imagen'], id = request.user.id)
#            imagen.save()
#            imagen = imagenes.objects.filter(user = request.user.id)
#            try:
#                imagen = imagen[0].image.url
#            except:
#                imagen = None           
#            return render(request, 'home.html', {'imagen': imagen})
#    else:
#        try:
#            avatar = imagenes.objects.filter(user = request.user.id)
#            form = ImagenFormulario()
#        except:
#            form = ImagenFormulario()
#    return render(request, 'AgregarAvatar.html', {'form': form})
#
def actualizar(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance = usuario)
        if formulario.is_valid():
            #Datos que se van a actualizar
            user_basic_info.username = formulario.cleaned_data.get('username')
            user_basic_info.email = formulario.cleaned_data.get('email')
            user_basic_info.first_name = formulario.cleaned_data.get('first_name')
            user_basic_info.last_name = formulario.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            usuario = request.user
            usuario =User.objects.filter(username__icontains= usuario.username) 
            return render(request, 'perfil.html', {'avatar': avatar, 'usuario': usuario})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            usuario = request.user
            usuario =User.objects.filter(username__icontains= usuario.username)                      
            return render(request, 'perfil.html', {'form':formulario, 'avatar': avatar, 'usuario': usuario})
    else:
        formulario = UserEditForm(initial={'email': usuario.email, 'username': usuario.username, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
    return render(request, 'actualizar.html', {'formulario': formulario, 'usuario': usuario})

def cambiarContraseña(request):
    usuario = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html', {'avatar': avatar})
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'cambiarContraseña.html', {'form': form, 'usuario': usuario})

def delete(request):
    usuario = 1
    if  usuario == 1:
        usuario = request.user
        usuario =User.objects.get(username__icontains= usuario.username) 
        usuario.delete()
        return render(request, "homelg.html")
    usuario = request.user
    usuario =User.objects.filter(username__icontains= usuario.username) 
    respuesta= {"usuario": usuario}
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "perfil.html", {"usuario": usuario, 'avatar': avatar})

def deletePost(request):
    post = 1
    if  post == 1:
        post= request.posteo
        post =Posteo.objects.filter(user_id__icontains= post.id) 
        post.delete()
        return render(request, "home.html")
    post=Posteo.objects.all()
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "home.html", {"post": post, 'avatar': avatar})