from django.shortcuts import render
from .models import Usuario
from .forms import registroUsuarios
from django.views.generic import CreateView

# Create your views here.
class RegistrarUsuarios(CreateView):
	model = Usuario
	form_class = registroUsuarios
	template_name = 'usuario/registrar.html'