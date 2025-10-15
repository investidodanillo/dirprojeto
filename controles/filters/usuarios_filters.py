# controles\filters\usuarios_filters.py
import django_filters
from django import forms
from django.contrib.auth.models import User


class UsuariosFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="ID",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Pesquisar por ID"
        })
    )

    username = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Usuário",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite o nome de usuário"
        })
    )

    # ✅ ChoiceFilter: criamos escolhas dinamicamente com distinct()
    first_name = django_filters.ChoiceFilter(
        choices=lambda: [(n, n) for n in User.objects.values_list('first_name', flat=True).distinct() if n],
        label="Nome",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    last_name = django_filters.ChoiceFilter(
        choices=lambda: [(n, n) for n in User.objects.values_list('last_name', flat=True).distinct() if n],
        label="Sobrenome",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    email = django_filters.ChoiceFilter(
        choices=lambda: [(n, n) for n in User.objects.values_list('email', flat=True).distinct() if n],
        label="Email",
        widget=forms.Select(attrs={"class": "form-control"})
    )
    
    is_active = django_filters.BooleanFilter(
        label="Ativo",
        widget=forms.Select(
            choices=[('', 'Todos'), ('true', 'Sim'), ('false', 'Não')],
            attrs={"class": "form-control"}
            )
        )

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]
        order_by = ['id']  # Ordenação padrão por ID
        per_page = 10  # Paginação: 10 registros por página