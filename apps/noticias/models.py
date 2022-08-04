from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.nombre

# Create your models here.
class Noticia(models.Model):
    #ID = ('ID',max_length = 99999)
    titulo = models.CharField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    #class Meta:
    #    verbose_name = 'Noticia'
    #    verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo
