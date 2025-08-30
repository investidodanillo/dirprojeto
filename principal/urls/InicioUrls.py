
# dirprojeto\aplicativo\urls\InicioUrls.py
from django.urls import path
from principal.views.inicio.index import principal_inicio_index_view

app_name = 'principal'

urlpatterns = [
    path('', principal_inicio_index_view, name='principal_inicio_index_view'),
    
        
]

