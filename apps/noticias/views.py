from django.shortcuts import render
from .models import Noticia, Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Create your views here.

class agregar(CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'activo', 'imagen']
    template_name = 'noticias/agregar.html'
    success_url = reverse_lazy('index')


class mostrar(ListView):
    model = Noticia
    template_name = 'noticias/mostrar.html'

def mostrarImg(request): # parecido a un get
    noticia = Noticia.objects.all()
    context = {
        'noticia' : noticia
    }
    return render(request,'noticias/mostrarImg.html',context)

def mostrarImgCat(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia = Noticia.objects.filter(categoria = categoria2[0].id)
    context = { 
		'noticia': noticia,
    }
    return render(request,'noticias/mostrarImg.html', context)