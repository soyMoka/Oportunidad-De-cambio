from django.db import models

# Create your models here.

class Usuario(ModeloBase):
    id = models.CharField('ID',max_length = 9999)
    nombre = models.CharField('Nombres',max_length = 100)
    apellidos = models.CharField('Apellidos',max_length = 120)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos,self.nombre)
