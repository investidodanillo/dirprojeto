import django_filters
from django import forms
from aplicativo.models.assunto04.models import (
    Produto,
) 


class ProdutoFilter(django_filters.FilterSet):
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
        label="Pesquisar Campo 2",
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite parte do Campo 2"
        })
    )
    
    quantidade = django_filters.NumberFilter(
        lookup_expr="icontains",
        label="Número Inteiro",
        widget=forms.NumberInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite o Número Inteiro"
        })
    )
    
    preco = django_filters.NumberFilter(
        lookup_expr="icontains",
        label="Número Decimal",
        widget=forms.NumberInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite o Número Decimal"
        })
    )
    
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'quantidade', 'preco']