from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date
import datetime

def user_directory_path(instance, filename):
    # Construye la ruta donde se guardará el archivo
    # La imagen se guardará en MEDIA_ROOT/images/{username}/{filename}
    return f'images/{instance.user.username}/{filename}'

class PerfilProfesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_profesor = models.CharField(max_length=50, default='Editar nombre de vendedor')
    image = models.ImageField(upload_to=user_directory_path, default='images/default.jpg')
    descripcion_profesor = models.TextField(max_length=255, blank=True, default='Editar profesor')
    biografia_profesor = models.TextField(max_length=255, blank=True, default='Editar profesor')

    def __str__(self):
        return self.nombre_profesor

    def save(self, *args, **kwargs):
        # Si la instancia ya tiene una imagen guardada, elimina el archivo anterior
        try:
            this = PerfilProfesor.objects.get(id=self.id)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="media/images")
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)
    def __str__(self):
        return f'Proyecto: {self.title}'
    

class Post(models.Model):
   # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=user_directory_path)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title