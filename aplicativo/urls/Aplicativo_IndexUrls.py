from django.urls import path
from aplicativo.views.aplicativo_index.aplicativo_indexViews import aplicativo_index_view

app_name = 'aplicativo_index'

urlpatterns = [
    path('aplicativo_index/', aplicativo_index_view, name='aplicativo_index'),
]


