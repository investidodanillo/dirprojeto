
# principal\urls\HomeUrls.py
from django.urls import path
from principal.views.inicio.home import home_inicio_View


app_name = 'home'

urlpatterns = [    
    path('home_inicio_View/', home_inicio_View, name='home_inicio_View'),
    
 
    
]

