# aplicativo\views\aplicativo_index\aplicativo_indexViews.py
from django.shortcuts import render

def desing_index_view(request):

    return render(request, 'desing_index.html')


