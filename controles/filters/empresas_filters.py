# controles\filters\usuarios_filters.py
import django_filters
from django import forms
from controles.models.empresas.Empresas_models import Empresas


class EmpresasFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="ID",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Pesquisar por ID"
        })
    )

    nome = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Usuário",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite o nome de usuário"
        })
    )


    cnpj = django_filters.CharFilter(
        lookup_expr="icontains",
        label="CNPJ",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite o CNPJ"
        })
    )

    data_criacao = django_filters.DateFilter(
        lookup_expr="icontains",
        label="Data de Criação",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite a data de criação"
        })
    )   

    ativa = django_filters.BooleanFilter(
        label="Ativo",
        widget=forms.Select(
            choices=[('', 'Todos'), ('true', 'Sim'), ('false', 'Não')],
            attrs={"class": "form-control"}
            )
        )     


    class Meta:
        model = Empresas
        fields = ["id", "nome", "cnpj", "data_criacao", "ativa"]
        order_by = ['id']  # Ordenação padrão por ID
        per_page = 10  # Paginação: 10 registros por página