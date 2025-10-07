from django.urls import path
from desing.views.desing_index.desing_indexViews import desing_index_view

app_name = 'desing_index'

urlpatterns = [
    path('desing_index/', desing_index_view, name='desing_index'),
]


