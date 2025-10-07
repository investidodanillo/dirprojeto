from django.shortcuts import render

def controles_index_view(request):
    return render(request, 'controles_index.html')