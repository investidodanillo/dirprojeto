#dirprojeto\desenvolvimento\forms\tabelas\forms.py
from django import forms
from desenvolvimento.models.boards.tabelas_boards_models import Categoria, Sistema

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 1, texto curto'}),
                   'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 1, texto curto'}),
                   'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo 5, texto longo'}),
                   }

class SistemaForm(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = '__all__'
        widgets = {'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 1, texto curto'}),
                   'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 1, texto curto'}),
                   'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo 5, texto longo'}),
                   }
        
