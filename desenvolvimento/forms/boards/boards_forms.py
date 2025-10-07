# dirprojeto\desenvolvimento\forms\tabelas\forms.py
from django import forms
from desenvolvimento.models.boards.BoardsPrincipal_models import ItemEvolucao, Release, ChecklistSistema, ChecklistItem
from desenvolvimento.models.boards.tabelas_boards_models import (
    Categoria,
    Sistema,
    TipoItem, 
    Prioridade, 
    Status)

class ItemEvolucaoForm(forms.ModelForm):
    class Meta:
        model = ItemEvolucao
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite o título do item'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Descreva detalhadamente o item',
                'rows': 4
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-control form-select'
            }),            
            'status': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'sistema': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'criado_por': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'responsavel': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'versao_prevista': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ex: v1.2'
            }),
            'data_conclusao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),         
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar placeholders específicos para campos choice
        self.fields['tipo'].empty_label = "Selecione o tipo"
        self.fields['prioridade'].empty_label = "Selecione a prioridade"
        self.fields['status'].empty_label = "Selecione o status"
        self.fields['sistema'].empty_label = "Selecione o sistema"
        self.fields['categoria'].empty_label = "Selecione a categoria"
        self.fields['criado_por'].empty_label = "Selecione quem criou"
        self.fields['responsavel'].empty_label = "Selecione o responsável"

class ReleaseForm(forms.ModelForm):
    class Meta:
        model = Release
        fields = '__all__'
        widgets = {            
            'sistema': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'versao': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite a versão (ex: v1.0.1)'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Descreva esta release',
                'rows': 4
            }),
            'itens': forms.SelectMultiple(attrs={
                'class': 'form-control form-select',
                'size': 6
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sistema'].empty_label = "Selecione o sistema"
        self.fields['itens'].help_text = "Segure Ctrl para selecionar múltiplos itens"

class ChecklistSistemaForm(forms.ModelForm):
    class Meta:
        model = ChecklistSistema
        fields = '__all__'
        widgets = {
            'sistema': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nome do checklist'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Descrição do checklist',
                'rows': 3
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sistema'].empty_label = "Selecione o sistema"

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = '__all__'
        widgets = {
            'checklist': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Descrição do item do checklist'
            }),
            'concluido': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['checklist'].empty_label = "Selecione o checklist"