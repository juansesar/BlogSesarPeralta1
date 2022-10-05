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

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render (request, "home.html")

def registro(request):
    if request.method == "POST":
        usuario= user(username = request.POST['username'], email = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'],password= request.POST['password'] )
        usuario.save()
        return render(request, "home.html")
    return render(request, "registro.html")

#def perfil(request):
#    return render (request, "perfil.html")

def perfil(request=None):
    usuario = user.objects.filter(username__icontains = usuario) 
    return render(request, "perfil.html", {"usuarios": usuario})

def fotoPerfil(request):
    return render (request, "fotoPerfil.html")

def experiencia(request):
    return render (request, "experiencia.html")

def actualizar(request):
    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario= user(username = informacion['username'], email = informacion['email'], first_name = informacion['first_name'], last_name = informacion['last_name'],password= informacion['password'] )
            usuario.save()
            return render (request, "perfil.html")
    else:
        formulario = UserEditForm()
    return render (request, "actualizar.html", {'formulario': formulario})
    

#def login(request):
#    return render (request, "login.html")

def login(request):
    #if request.GET["email"] and request.GET["password"]:
    #    email = request.GET["email"]
    #    usuarios = user.objects.filter(email__icontains = email) 
    #    pwd = request.GET["password"]
    #    password = user.objects.filter(pasword__icontains = password)
    #    if email == usuarios and pwd == password:
    #        return render(request, "inicio.html")
    #else:
    #    respuesta = "No enviaste datos"
    return render (request, "login.html")





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
##@login_required
##def AgregarAvatar(request):
#    if request.method == 'POST':
#        form = AvatarFormulario(request.POST, request.FILES)
#        print(form)
#        print(form.is_valid())
#        if form.is_valid():
#            user = User.objects.get(username = request.user)
#            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
#            avatar.save()
#            avatar = Avatar.objects.filter(user = request.user.id)
#            try:
#                avatar = avatar[0].image.url
#            except:
#                avatar = None           
#            return render(request, 'home.html', {'avatar': avatar})
#    else:
#        try:
#            avatar = Avatar.objects.filter(user = request.user.id)
#            form = AvatarFormulario()
#        except:
#            form = AvatarFormulario()
#    return render(request, 'AgregarAvatar.html', {'form': form})
#