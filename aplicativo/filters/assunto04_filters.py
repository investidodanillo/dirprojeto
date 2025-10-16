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
        label="NOME",
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite parte do NOME"
        })
    )
    
    quantidade = django_filters.NumberFilter(
        lookup_expr="icontains",
        label="QUANTIDADE",
        widget=forms.NumberInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite a QUANTIDADE"
        })
    )
    
    preco = django_filters.NumberFilter(
        lookup_expr="icontains",
        label="PREÇO",
        widget=forms.NumberInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite o PREÇO"
        })
    )
    
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'quantidade', 'preco']