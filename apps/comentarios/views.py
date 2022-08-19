from django.shortcuts import render

# Create your views here.

def AddComentario(request):
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)
