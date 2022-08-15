from django.urls import path
from .views import BorrarNoticia
from . import views
app_name = 'apps.noticia'

urlpatterns = [
    path('agregar/', views.agregar.as_view(), name = 'agregar'),
    path('mostrar/', views.mostrar.as_view(), name = 'mostrar'),
    path('', views.mostrar.as_view()),
    path('borrar/<int:pk>', BorrarNoticia.as_view(), name= 'borrar_noticia'),
    path('mostrarImg/', views.mostrarImg,name = 'mostrarImg'),
    path('mostrarImg/<str:categoria>', views.mostrarImgCat, name="mostrarCategoria"),
]