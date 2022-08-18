from mailbox import NoSuchMailboxError
from unicodedata import name
from django.shortcuts import render

from apps import noticias
from .models import Noticia, Categoria
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
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

    # Lista de noticias
    #noticia = Noticia.objects.all()
    noticia = Noticia.objects.order_by("-fecha")
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


class mostrarDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'noticias/mostrarDetalleNoticia.html'


#||CATEGORIAS --------------------------------#
class agregarCategoriaView(CreateView):
    model = Categoria
    template_name = 'noticias/agregarCategoria.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Categoria.objects.all()
        context = super(agregarCategoriaView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return  context

#-_-_-_-_-_-_-_-_-_| separador |_-_-_-_-_-_-_-_-_-

def CategoryList(request, cates):
    
    cat = Categoria.objects.filter( nombre = cates)
    if len(cat) > 0:
        noticiasFiltradas = Noticia.objects.filter(categoria = cat[0].id)
    c = []
    for dic in Categoria.objects.values('nombre'):
        
        c.append(dic['nombre'])
        

    myContext = {
        'c': c,
        'cates':cates, 
        'noticiasFiltradas':noticiasFiltradas,
    }    

        
    return render(request, 'noticias/filtrarPorCategoria.html', myContext )

#------------------ END CATEGORIAS ---------------------#




