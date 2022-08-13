from django.urls import path

from . import views
app_name = 'apps.noticia'

urlpatterns = [
    path('agregar/', views.agregar.as_view()),
    path('mostrar/', views.mostrar.as_view()),
    path('', views.mostrar.as_view()),
    path('mostrarImg/', views.mostrarImg),
    path('mostrarImg/<str:categoria>', views.mostrarImgCat, name="mostrarCategoria"),
]