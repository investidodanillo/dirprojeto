#principal\views\inicio\index.py
from django.shortcuts import render


def principal_inicio_index_view(request):
    return render(request, 'inicio/index.html')