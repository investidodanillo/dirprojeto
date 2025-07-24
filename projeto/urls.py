from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     
    path('', include('aplicativo.urls.InicioUrls')),
    path('', include('aplicativo.urls.Assunto01Urls')),
    path('', include('aplicativo.urls.Assunto02Urls')),
    path('', include('aplicativo.urls.Assunto03Urls')),

]