from django.shortcuts import render, redirect
from .models import Project, PerfilProfesor
from .forms import Postform, PerfilProfesorForm, RegistroForm



from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, PerfilProfesor

@login_required
def home(request):
    # Obtén el perfil del usuario logeado actual o devuelve un error 404 si no existe
    perfil = get_object_or_404(PerfilProfesor, user=request.user)

    # Deja el queryset de proyectos vacío
    projects = []

    context = {
        'projects': projects,
        'perfil': perfil,
    }
    return render(request, "home.html", context)
def perfil(request):
    # Obtén el perfil del usuario logeado actual o devuelve un error 404 si no existe
    perfil = get_object_or_404(PerfilProfesor, user=request.user)

    # Obtén todos los proyectos
    projects = []

    context = {
        'projects': projects,
        'perfil': perfil,
        'en_perfil': True,
    }
    return render(request, "perfil.html", context)

def crear_publicacion(request):

    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Postform()
    context = {
        'form': form
    }
    return render(request, "portafolio/crear_portafolio.html", context)


@login_required
def editar_perfil(request):
    # Obtén el perfil existente si ya hay uno para este usuario
    perfil_profe = get_object_or_404(PerfilProfesor, user=request.user)

    if request.method == 'POST':
        form = PerfilProfesorForm(request.POST, request.FILES, instance=perfil_profe)
        if form.is_valid():
            # Guarda los datos del formulario en el perfil del profesor
            form.save()
            return redirect('home')
    else:
        # Inicializa el formulario con los datos del perfil del profesor
        form = PerfilProfesorForm()

    context = {
        'form': form,
        'perfil_profe': perfil_profe,
    }
    return render(request, "portafolio/profesor.html", context)


def logout(request):
    return redirect('login')

from django.db import transaction
from .forms import RegistroForm, PerfilProfesorForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        form2 = PerfilProfesorForm(request.POST)
        
        if form.is_valid() and form2.is_valid():
            user = form.save()  # Guarda el usuario y obtén el objeto User
            perfil_profesor = form2.save(commit=False)
            perfil_profesor.user = user  # Asigna el usuario al perfil de profesor
            perfil_profesor.save()

            # Redirige a la página de inicio o a donde desees después del registro.
            return redirect('home')
    else:
        form = RegistroForm()
        form2 = PerfilProfesorForm()
        
    context = {
        'form': form,
        'form2': form2
    }
    return render(request, 'registro.html', context)
