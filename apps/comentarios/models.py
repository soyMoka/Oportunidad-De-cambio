from django.db import models
from apps import Noticia
from apps import Usuario
#from apps.usuarios.models import Usuario
# Create your models here.

# si llega a haber algun problema aca, entonces es el from apps...

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_created=True)
    

