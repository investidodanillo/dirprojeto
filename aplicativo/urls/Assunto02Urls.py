#dirprojeto\aplicativo\urls\Assunto02Urls.py
from django.urls import path
from aplicativo.views.assunto02.assunto02_capitulo01_View import (
     assunto02_capitulo01_View_index,
     assunto02_capitulo01_View_inicio,
     assunto02_capitulo01_cadastro_View,
     assunto02_Capitulo01_Update_View,
     
     assunto02_capitulo01_visualizar_View,
     
)
app_name = 'assunto02'


urlpatterns = [
    path('assunto02_capitulo01_View_index/', assunto02_capitulo01_View_index, name='assunto02_capitulo01_View_index'),
    path('assunto02_capitulo01_View_inicio/', assunto02_capitulo01_View_inicio, name='assunto02_capitulo01_View_inicio'),
    #Cadastro de Assunto02 Capitulo01 View
    # URL para criar um novo objeto (CreateView)
    # Cadastro (CreateView)
    path('assunto02_capitulo01_cadastro_View/', 
         assunto02_capitulo01_cadastro_View.as_view(), 
         name='assunto02_capitulo01_cadastro_View'),

    
    path('assunto02_Capitulo01_Update_View/<int:pk>/', 
         assunto02_Capitulo01_Update_View.as_view(), 
         name='assunto02_Capitulo01_Update_View'),

 
     
     path('assunto02_capitulo01_visualizar_View/',
         assunto02_capitulo01_visualizar_View.as_view(),
         name='assunto02_capitulo01_visualizar_View'),


]

