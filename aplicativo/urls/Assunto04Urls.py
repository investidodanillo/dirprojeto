#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from aplicativo.views.assunto04.assunto04_capitulo01_View import(
     assunto04_index, 
     assunto04_capitulo01_inicio_views, 
     assunto04_capitulo01_cadastro_View, 
     assunto04_Capitulo01_Update_View,    
     assunto04_capitulo01_ProdutoListViewTab,
)

app_name = 'assunto04'


urlpatterns = [
    path('assunto04_index/', assunto04_index, name='assunto04_index'),
    path('assunto04_capitulo01_inicio/', assunto04_capitulo01_inicio_views, name='assunto04_capitulo01_inicio'),
 

    path('assunto04_capitulo01_cadastro/', assunto04_capitulo01_cadastro_View.as_view(), name='assunto04_capitulo01_cadastro'),
    path('assunto04_Capitulo01_Update/<int:pk>/', assunto04_Capitulo01_Update_View.as_view(), name='assunto04_Capitulo01_Update'),
    path('assunto04_capitulo01_ProdutoListViewTab/', assunto04_capitulo01_ProdutoListViewTab.as_view(), name='assunto04_capitulo01_ProdutoListViewTab'),

   


]

