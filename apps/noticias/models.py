from django.db import models

# Create your models here.
class Noticia(ModeloBase):
    ID = ('ID',max_length = 99999)
    titulo = models.CharField('Título del Post',max_length = 150, unique = True)
    fecha = models.DateField('fecha')
    texto = RichTextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo
