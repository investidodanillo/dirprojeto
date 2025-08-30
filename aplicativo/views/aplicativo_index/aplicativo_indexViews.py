from django.shortcuts import render

def aplicativo_index_view(request):
    return render(request, 'aplicativo_index.html')