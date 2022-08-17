from django.urls import path
from .views import BorrarNoticia
from . import views

from django.conf.urls import include, url

app_name = 'apps.noticia'

urlpatterns = [
    path('agregar/', views.agregar.as_view(), name = 'agregar'),
    path('mostrar/', views.mostrar.as_view(), name = 'mostrar'),
    path('', views.mostrar.as_view()),
    path('modificar/<int:pk>',views.modificar.as_view(), name = 'modificar'),
    path('borrar/<int:pk>', BorrarNoticia.as_view(), name= 'borrar'),
    path('mostrarImg/', views.mostrarImg,name = 'mostrarImg'),
    path('mostrarImg/<str:categoria>', views.mostrarImgCat, name="mostrarCategoria"),
    path('mostrarCategorias/', views.mostrarCategorias,name = 'mostrarCategorias'),
    path('detalle/<int:pk>', views.mostrarDetalleNoticia.as_view(), name= 'mostrarDetalleNoticia'),
    
]