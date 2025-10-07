from django.shortcuts import render

def desenvolvimento_index_view(request):
    return render(request, 'desenvolvimento_index.html')