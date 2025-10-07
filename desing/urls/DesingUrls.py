#dirprojeto\aplicativo\urls\Assunto02Urls.py
from django.urls import path
from desing.views.desing_inicio.desing_inicio_View import (
     desing_capitulo01_View_index,
     desing_capitulo01_View_inicio,
     desing_modelo_View,
     desing_Typography_View,
     desing_Forms_View,
     desing_Buttons_View,
     desing_Cards_View,
     desing_Tables_View,
     desing_Badges_View,

     
     
)

app_name = 'desing'


urlpatterns = [
     path('desing_capitulo01_View_index/', desing_capitulo01_View_index, name='desing_capitulo01_View_index'),
     path('desing_capitulo01_View_inicio/', desing_capitulo01_View_inicio, name='desing_capitulo01_View_inicio'),
     path('desing_modelo/', desing_modelo_View, name='desing_modelo'),

     path('desing_Typography_View/', desing_Typography_View, name='desing_Typography_View'),
     path('desing_Forms_View/', desing_Forms_View, name='desing_Forms_View'),
     path('desing_Buttons_View/', desing_Buttons_View, name='desing_Buttons_View'),
     path('desing_Cards_View/', desing_Cards_View, name='desing_Cards_View'),
     path('desing_Tables_View/', desing_Tables_View, name='desing_Tables_View'),
     path('desing_Badges_View/', desing_Badges_View, name='desing_Badges_View'),

                                       



     

    
]

