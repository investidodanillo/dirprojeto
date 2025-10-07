#dirprojeto\aplicativo\urls\Assunto01Urls.py
from django.urls import path
from aplicativo.views.assunto01.Capitulo01View import assunto01_capitulo01_View_index, assunto01_Capítulo01_inicio_view, assunto01_capitulo01_titulo01_view

app_name = 'assunto01'


urlpatterns = [
    path('assunto01_capitulo01_View_index/', assunto01_capitulo01_View_index, name='assunto01_capitulo01_View_index'),
    path('assunto01_Capítulo01_inicio/', assunto01_Capítulo01_inicio_view, name='assunto01_Capítulo01_inicio'),
    path('assunto01_capitulo01_titulo01/', assunto01_capitulo01_titulo01_view, name='assunto01_capitulo01_titulo01'),
]


