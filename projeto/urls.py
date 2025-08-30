# projeto\urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #public
    path('', include('principal.urls.InicioUrls')),
    path('', include('principal.urls.HomeUrls')), 
    # Auth
    path('', include('principal.urls.auth')),

    #index aplicativo
    path('', include('aplicativo.urls.Aplicativo_IndexUrls')),
     

    path('', include('aplicativo.urls.Assunto01Urls')),
    path('', include('aplicativo.urls.Assunto02Urls')),
    path('', include('aplicativo.urls.Assunto03Urls')),   
   

]