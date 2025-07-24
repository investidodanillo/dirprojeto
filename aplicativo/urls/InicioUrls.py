
# dirprojeto\aplicativo\urls\InicioUrls.py
from django.urls import path
from aplicativo.views.inicio.index import inicio_index_view
from aplicativo.views.inicio.home import inicio_home_View


app_name = 'inicio'
urlpatterns = [
    path('', inicio_index_view, name='inicio_index_view'),
    path('inicio_home_View/', inicio_home_View, name='inicio_home_View'),
    


    
    
]

