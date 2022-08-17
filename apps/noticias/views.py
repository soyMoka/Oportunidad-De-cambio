from mailbox import NoSuchMailboxError
from unicodedata import name
from django.shortcuts import render
from .models import Noticia, Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
# Create your views here.


# ListaDenoticias = Noticia.objects.first()
# TituloCategoria = Noticia.Categoria
# Categorias = Noticia.objects.first()
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def mostrarCategorias(request):
    categories = Categoria.objects.all() # this will get all categories, you can do some filtering if you need (e.g. excluding categories without posts in it)
    return render (request, 'noticias/mostrarCategorias.html', {'categories': categories}) # blog/category_list.html should be the template that categories are listed.

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


class BorrarNoticia(DeleteView):
    model = Noticia
    template_name = 'noticias/borrar.html'
    success_url = reverse_lazy('index')
    
    
    
class modificar(UpdateView):
    model = Noticia
    fields = ['titulo', 'texto', 'categoria', 'imagen']
    template_name = 'noticias/modificar.html'
    success_url = reverse_lazy('index')