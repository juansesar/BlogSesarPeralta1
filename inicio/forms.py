from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="", widget= forms.PasswordInput(attrs={'placeholder': "Old Password"}))
    new_password1 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "New password"}))
    new_password2 = forms.CharField(label="",widget= forms.PasswordInput(attrs={'placeholder': "Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}
#

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()

class ImagenFormulario(forms.Form):
    imagen = forms.ImageField()

class PostEditForm(forms.Form):
    titulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'titulo'}))
    subtitulo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'subtitulo'}))
    cuerpo = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'cuerpo'}))
    fecha = forms.DateField(widget= forms.TextInput(attrs={'placeholder': 'fecha'}))
    image = forms.ImageField(widget= forms.FileInput(attrs={'placeholder': 'foto'}))
    
class mensajesForm(forms.Form):
    mensaje=forms.CharField(label="deja un mensáje para este post")
    
        
    