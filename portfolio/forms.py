from django import forms
from .models import Project, PerfilProfesor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'Username'

    }), required=True)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'floatingInput',
        'placeholder':'user@example.com',
        
    }), required=True)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'floatingPassword',
        'placeholder':'Contraseña',
        
    }), required=True)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'id':'floatingPassword',
        'placeholder':'Confirma contraseña',
        
    }), required=True)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

        
class Postform(forms.ModelForm):

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'id':'floatingInput',


    }), required=True)
    description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'floatingTextarea2',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'type':'file',
        'id':'formFileMultiple',


    }))
    url = forms.URLField(widget=forms.URLInput(attrs={
        'class':'form-control',
        'type':'url',
        'id':'floatingInput',

    }),required=False)
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url']

class PerfilProfesorForm(forms.ModelForm):

    nombre_profesor = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',
        'id':'floatingInput',
        'type':'text',

    }), required=True)

    descripcion_profesor = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control',
        'id':'floatingarea',
        'type':'text',

    }), required=True)

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control',
        'type':'file',
        'id':'formFileMultiple',


    }), required = False)

    biografia_profesor = forms.CharField(widget=forms.Textarea(attrs={

        'class': 'form-control',
        'id':'floatingarea3',
        'type':'text',
            
    }), required=True)

    class Meta:
        model = PerfilProfesor
        fields = ['nombre_profesor', 'descripcion_profesor','image', 'biografia_profesor']