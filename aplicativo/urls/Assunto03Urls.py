#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from aplicativo.views.assunto03.assunto03_capitulo01_View import(
     assunto03_index_View, 
     assunto03_capitulo01_View_inicio, 


     assunto03_capitulo01_cadastro_View, 
     assunto03_Capitulo01_Update_View,    
     assunto03_capitulo01_visualizar_View,
     

     assunto03_capitulo01_cadastro_TabelaSis2_View,
     assunto03_Capitulo01_Update2_View,     
     assunto03_capitulo01_visualizar2_View,
  


)

app_name = 'assunto03'


urlpatterns = [
    path('assunto03_index_View/', assunto03_index_View, name='assunto03_index_View'),
    path('assunto03_capitulo01_View_inicio/', assunto03_capitulo01_View_inicio, name='assunto03_capitulo01_View_inicio'),
    #01

    path('assunto03_capitulo01_cadastro_View/', assunto03_capitulo01_cadastro_View.as_view(), name='assunto03_capitulo01_cadastro_View'),
    path('assunto03_Capitulo01_Update_View/<int:pk>/', assunto03_Capitulo01_Update_View.as_view(), name='assunto03_Capitulo01_Update_View'),
    path('assunto03_capitulo01_visualizar_View/', assunto03_capitulo01_visualizar_View.as_view(), name='assunto03_capitulo01_visualizar_View'),

    #02


    # URL para criar um novo objeto (CreateView)
    path('assunto03_capitulo01_cadastro_TabelaSis2_View/', assunto03_capitulo01_cadastro_TabelaSis2_View.as_view(), name='assunto03_capitulo01_cadastro_TabelaSis2_View'),
    path('assunto03_Capitulo01_Update2_View/<int:pk>/', assunto03_Capitulo01_Update2_View.as_view(), name='assunto03_Capitulo01_Update2_View'),
    path('assunto03_capitulo01_visualizar2_View/', assunto03_capitulo01_visualizar2_View.as_view(), name='assunto03_capitulo01_visualizar2_View'),


]

