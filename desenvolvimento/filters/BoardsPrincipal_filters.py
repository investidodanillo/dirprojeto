# desenvolvimento/filters/BoardsPrincipal_filters.py
import django_filters
from django import forms
from desenvolvimento.models.boards.BoardsPrincipal_models import ItemEvolucao, ChecklistSistema, ChecklistItem, Release

# ITEM EVOLUÇÃO
class BoardsPrincipal_ItemEvolucao_Filter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar ID",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do ID"}
        ),
    )    
    titulo = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Título",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do título"}
        ),
    )
    tipo = django_filters.ChoiceFilter(
        choices=ItemEvolucao._meta.get_field("tipo").choices,
        label="Tipo",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    status = django_filters.ChoiceFilter(
        choices=ItemEvolucao._meta.get_field("status").choices,
        label="Status",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    sistema = django_filters.CharFilter(
        field_name="sistema__nome",
        lookup_expr="icontains",
        label="Sistema",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do sistema"}
        ),
    )
    versao_prevista = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Versão Prevista",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte da versão"}
        ),
    )
    data_criacao = django_filters.DateFilter(
        field_name="data_criacao",
        lookup_expr="exact",
        label="Data de Criação",
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}
        ),
    )
    data_conclusao = django_filters.DateFilter(
        field_name="data_conclusao",
        lookup_expr="exact",
        label="Data de Conclusão",
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}
        ),
    )

    class Meta:
        model = ItemEvolucao
        fields = ["id", "titulo", "tipo", "status", "sistema"]

# CHECKLIST SISTEMA
class BoardsPrincipal_ChecklistSistema_Filter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="ID",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do ID"}
        ),
    )
    sistema=django_filters.CharFilter(
        field_name="sistema__nome",
        lookup_expr="icontains",
        label="Sistema",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do sistema"}
        ),
    )

    nome = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Nome",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do nome"}
        ),
    )
    ativo = django_filters.BooleanFilter(
        label="Ativo",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        field_name="ativo",
        lookup_expr="exact",

    )    

    class Meta:
        model = ChecklistSistema
        fields = ["id", "sistema", "nome", "ativo"]

class BoardsPrincipal_ChecklistItem_Filter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar ID",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do ID"}
        ),
    )

    nome = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Nome",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do nome"}
        ),
    )


    class Meta:
        model = ChecklistItem
        fields = ["id", "nome"]

class BoardsPrincipal_Release_Filter(django_filters.FilterSet):
    id = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar ID",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do ID"}
        ),
    )

    sistema = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Sistema",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte do sistema"}
        ),
    )

    versao = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Pesquisar Versão",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Digite parte da versão"}
        ),
    )

    data = django_filters.DateFilter(
        field_name="data",
        lookup_expr="exact",
        label="Data",
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "date"}
        ),
    )

    class Meta:
        model = Release
        fields = ["id", "sistema", "versao", "data"]

    