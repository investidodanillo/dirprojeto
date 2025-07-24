#dirprojeto\aplicativo\views\assunto01\capitulo01View.py
from django.shortcuts import render
from django.http import HttpResponse

def inicio_index_view(request):
    return render(request, 'inicio/index.html')




