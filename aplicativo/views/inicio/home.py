#dirprojeto\aplicativo\views\assunto01\capitulo01View.py
from django.shortcuts import render
from django.http import HttpResponse

def inicio_home_View(request):
    return render(request, 'inicio/home.html')




