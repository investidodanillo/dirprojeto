from django.urls import path
from desenvolvimento.views.desenvolvimento_index.Desenvolvimento_Index_Views import desenvolvimento_index_view


app_name = 'desenvolvimento_index'

urlpatterns = [
    path('desenvolvimento_index/', desenvolvimento_index_view, name='desenvolvimento_index'),
]