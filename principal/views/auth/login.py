# principal\views\auth\login.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home:home_inicio_View")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

# LOGOUT VIEW
def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta com sucesso.")
    return redirect("principal:principal_inicio_index_view")





