#principal\views\inicio\home.py
from django.shortcuts import render
from django.http import HttpResponse

def home_inicio_View(request):
    return render(request, 'inicio/home.html')

# principal\templates\base_home.html