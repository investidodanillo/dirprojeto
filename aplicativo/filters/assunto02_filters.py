import django_filters
from django import forms
from aplicativo.models.assunto02.models import Tabela1


class Tabela1Filter(django_filters.FilterSet):
    campo1 = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Campo 1",
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite parte do Campo 1"
        })
    )
    
    campo2 = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Campo 2",
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Digite parte do Campo 2"
        })
    )
    
    campo3 = django_filters.ChoiceFilter(
        choices=Tabela1.CONFIRMA,
        label="Confirmação",
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    
    campo4 = django_filters.BooleanFilter(
        label="Status Ativo",
        widget=forms.Select(
            choices=[('', 'Todos'), ('true', 'Sim'), ('false', 'Não')],
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Tabela1
        fields = ["id", "campo1", "campo2", "campo3", "campo4"]