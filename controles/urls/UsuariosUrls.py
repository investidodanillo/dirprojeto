#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from controles.views.Controles_Index.Controles_Usuarios_View import(
    controles_usuarios_View_inicio,
    controles_usuarios_View_index,

    controles_usuarios_cadastro_View,
    controles_usuarios_Update_View,
    controles_usuarios_visualizar_View

)

app_name = 'usuarios'


urlpatterns = [
    path('controles_usuarios_index/', controles_usuarios_View_index, name='controles_usuarios_View_index'),
    path('controles_usuarios_inicio/', controles_usuarios_View_inicio, name='controles_usuarios_View_inicio'),
    path('controles_usuarios_cadastro/', controles_usuarios_cadastro_View.as_view(), name='controles_usuarios_cadastro'),
    
    path('controles_usuarios_Update/<int:pk>/', controles_usuarios_Update_View.as_view(), name='controles_usuarios_Update_View'),

    path('controles_usuarios_visualizar/', controles_usuarios_visualizar_View.as_view(), name='controles_usuarios_visualizar'),
   

]

