from django.urls import path
from controles.views.Controles_Index import controles_index_view

app_name = 'controles_index'

urlpatterns = [
    path('controles_index/', controles_index_view, name='controles_index'),
]


