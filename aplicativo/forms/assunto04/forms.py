# dirprojeto\aplicativo\forms\assunto02\ModelForm.py
# dirprojeto/aplicativo/forms/assunto02/ModelForm.py
from django import forms
from aplicativo.models.assunto04.models import (
    Produto,
     )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'nome do produto'
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'descrição do produto',
                'class': 'form-control form-textarea',
                'rows': 4
            }),
            
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'quantidade do produto',
                'class': 'form-control'
            }),

            'preco': forms.NumberInput(attrs={
                'placeholder': 'preço do produto',
                'class': 'form-control',
                'step': '0.01'
            }),
        }

