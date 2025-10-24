#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from controles.views.empresas.Controles_Empresas_Views import(
    controles_empresas_View_index,
    controles_empresas_View_inicio,
#
    controles_empresas_cadastro_View,
    controles_empresas_Update_View,
    Controles_empresas_ListViewTab,

    )

app_name = 'empresas'


urlpatterns = [
    path('controles_empresas_index/', controles_empresas_View_index, name='controles_empresas_index'),
    path('controles_empresas_inicio/', controles_empresas_View_inicio, name='controles_empresas_inicio'),
    path('controles_empresas_cadastro/', controles_empresas_cadastro_View.as_view(), name='controles_empresas_cadastro'),    
    path('controles_empresas_Update/<int:pk>/', controles_empresas_Update_View.as_view(), name='controles_empresas_Update'),
    path('Controles_empresas_ListViewTab/', Controles_empresas_ListViewTab.as_view(), name='Controles_empresas_ListViewTab'),


  ]

