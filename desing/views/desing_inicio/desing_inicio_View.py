#dirprojeto\aplicativo\views\assunto03\assunto03_capitulo01_View.py
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from aplicativo.models.assunto03 import TabelaSis1, TabelaSis2
from aplicativo.forms.assunto03.forms import TabelaSis1Form, TabelaSis2Form
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def desing_capitulo01_View_index(request):
    return render(request, 'inicio_desing/index.html')

def desing_capitulo01_View_inicio(request):
    return render(request, 'inicio_desing/capitulo01/titulos/inicio.html')

def desing_modelo_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/desing_modelo.html')

def desing_Typography_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Typography.html')

def desing_Forms_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Forms.html')
def desing_Buttons_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Buttons.html')

def desing_Cards_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Cards.html')

def desing_Tables_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Tables.html')
def desing_Badges_View(request):
    return render(request, 'inicio_desing/capitulo01/titulos/Badges.html')