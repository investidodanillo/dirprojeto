#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from aplicativo.views.assunto01.Capitulo01View import assunto01_capitulo01_View_index, assunto01_inicio, capitulo01_inicio

app_name = 'assunto01'


urlpatterns = [
    path('assunto01_capitulo01_View_index/', assunto01_capitulo01_View_index, name='assunto01_capitulo01_View_index'),
    path('assunto01_inicio/', assunto01_inicio, name='assunto01_inicio'),
    path('capitulo01_inicio/', capitulo01_inicio, name='capitulo01_inicio'),
]


