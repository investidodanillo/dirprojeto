from django.urls import path
from principal.views.auth.login import login_view, logout_view
app_name="auth"

urlpatterns = [
    path("login/", login_view, name="login"),
    #path("logout/", logout_view, name="logout"),
]
