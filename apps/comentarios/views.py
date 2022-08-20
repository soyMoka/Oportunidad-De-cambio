from django.shortcuts import render

# Create your views here.

def AddComentario(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CommentForm()
	context={
		'form': form,
	}
	return render(request,'comentario/addcomentario.html', context)


