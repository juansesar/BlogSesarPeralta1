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

# Create your views here.
def home(request):
    return render (request, "home.html")

def homelg(request):
    return render (request, "homelg.html")

def CvSesar(request):
    return render (request, "CvSesar.html")

def CvPeralta(request):
    return render (request, "CvPeralta.html")

#def registro(request):
#    if request.method == "POST":
#        usuario= user(usern = request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'] )
#        usuario.save()
#        return render(request, "userForm.html")
#    return render(request, "registro.html")

#def perfil(request):
#    return render (request, "perfil.html")

def perfil(request=None):
    usuarios = User.objects.filter(username__icontains = usuarios) 
    return render(request, "perfil.html", {"usuarios": usuarios})

def perfilView(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'perfil.html', {'avatar': avatar})

def fotoPerfil(request):
    return render (request, "fotoPerfil.html")

def experiencia(request):

    return render (request, "experiencia.html")

def actualizar(request):
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario= User(username = informacion['username'], email = informacion['email'], first_name = informacion['first_name'], last_name = informacion['last_name'],password= informacion['password'] )
            usuario.save()
            return render (request, "perfil.html")
    else:
        formulario = UserEditForm()
    formulario = UserEditForm()
    return render (request, "actualizar.html", {'formulario': formulario})
    
def registro(request):  
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
                form.save()
                return render (request, "homelg.html")
        else:
            return render(request, "registro.html", {'form': form})  
    form = UserRegisterForm()
    return render(request, "registro.html", {'form': form})  

#def login(request):
#    return render (request, "login.html")

def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get('username')
            pwd = formulario.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)
            return render(request, 'home.html')
            #if user is not None:
            #    login(request, user)
            #    avatar = Avatar.objects.filter(user = request.user.id)
            #    try:
            #        avatar = avatar[0].image.url
            #    except:
            #        avatar = None
            #    return render(request, 'home.html', {'avatar': avatar})
            #else:
            #    return render(request, "login.html", {'formulario':formulario})
        else:
            return render(request, "login.html", {'formulario':formulario})
    formulario = AuthenticationForm()
    return render(request, 'login.html', {'formulario': formulario})

@login_required
def AgregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, 'home.html', {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarFormulario()
        except:
            form = AvatarFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})           
    
def newpost(request): 
    #datosdefault= Posteo(titulo= "titulo", subtitulo= "subtitulo", cuerpo= "comenta algo sobre esta foto", fecha= "fecha de la foto")
    #datoscargados= Posteo(request.POST)
    if request.method == 'POST':
        formulario = Posteo(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            post= Posteo(image = informacion['imagen'], titulo= informacion['titulo'], subtitulo= informacion['subtitulo'], cuerpo= informacion['cuerpo'], fecha= informacion['fecha'])
            post.save()
            return render (request, "home.html")
        else:
            "faltan datos"
    #if request.method == 'POST':
    #    form = ImagenFormulario(request.POST, request.FILES)
    #    print(form)
    #    print(form.is_valid())
    #    if form.is_valid():
    #        imagen = imagenes( imagen = form.cleaned_data['imagen'], id = request.user.id)
    #        imagen.save()
    #        imagen = imagenes.objects.filter(user = request.user.id)
    #        try:
    #            imagen = imagen[0].image.url
    #        except:
    #            aimagen = None           
    #        return render(request, 'home.html', {'imagen': imagen})
    #else:
    #    try:
    #        imagen = imagenes.objects.filter(user = request.user.id)
    #        form = ImagenFormulario()
    #    except:
    #        form = ImagenFormulario()
      
    return render (request, "newpost.html") 

def verpost(request=None):
    post = Posteo.objects.filter(username__icontains = post) 
    imagen = imagenes.objects.filter(user = request.user.id)
    return render(request, "perfil.html", {"post": post, 'imagen': imagen})   





#
#def login_request(request):
#    if request.method == 'POST':
#        form = AuthenticationForm(request, data = request.POST)
#        if form.is_valid():
#            user = form.cleaned_data.get('username')
#            pwd = form.cleaned_data.get('password')
#
#            user = authenticate(username = user, password = pwd)
#
#            if user is not None:
#                login(request, user)
#                avatar = Avatar.objects.filter(user = request.user.id)
#                try:
#                    avatar = avatar[0].image.url
#                except:
#                    avatar = None
#                return render(request, 'home.html', {'avatar': avatar})
#            else:
#                return render(request, "login.html", {'form':form})
#        else:
#            return render(request, "login.html", {'form':form})
#    form = AuthenticationForm()
#    return render(request, 'login.html', {'form': form})
#
#@login_required
#def home(request):
#    avatar = Avatar.objects.filter(user = request.user.id)
#    try:
#        avatar = avatar[0].image.url
#    except:
#        avatar = None
#
#    return render(request, 'home.html', {'avatar':avatar})
#
@login_required
def Agregarimagen(request):
    if request.method == 'POST':
        form = ImagenFormulario(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            imagen = imagenes( imagen = form.cleaned_data['imagen'], id = request.user.id)
            imagen.save()
            imagen = imagenes.objects.filter(user = request.user.id)
            try:
                imagen = imagen[0].image.url
            except:
                aimagen = None           
            return render(request, 'home.html', {'imagen': imagen})
    else:
        try:
            avatar = imagenes.objects.filter(user = request.user.id)
            form = ImagenFormulario()
        except:
            form = ImagenFormulario()
    return render(request, 'AgregarAvatar.html', {'form': form})