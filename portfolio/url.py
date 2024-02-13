from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('crear_publicacion/', views.crear_publicacion, name="crear_publicacion"),
    path('home/',  views.home, name='home'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('logout', views.logout, name = 'logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/',  views.perfil, name='perfil'),    
]