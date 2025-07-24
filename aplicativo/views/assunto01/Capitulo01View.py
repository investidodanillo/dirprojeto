#dirprojeto\aplicativo\views\assunto01\capitulo01View.py
from django.shortcuts import render

def assunto01_index(request):
    return render(request, 'assunto01/index.html')

def assunto01_inicio(request):
    return render(request, 'assunto01/capitulo01/titulos/inicio.html')

def capitulo01_inicio(request):
    return render(request, 'assunto01/capitulo01/titulos/inicio.html')


