from django.http import HttpResponse


from django.shortcuts import render

def saludo(request):
	contexto = {'mensaje': 'Hola Django - Coder'}
	return render(request, 'miApp/saludo.html', contexto)
