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
                'placeholder': 'Digite o Campo 1, texto curto'
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Campo de Texto Longo. TextField.',
                'class': 'form-control form-textarea',
                'rows': 4
            }),
            
            'quantidade': forms.NumberInput(attrs={
                'placeholder': 'Número Inteiro. IntegerField.',
                'class': 'form-control'
            }),

            'preco': forms.NumberInput(attrs={
                'placeholder': 'Número Decimal. FloatField.',
                'class': 'form-control',
                'step': '0.01'
            }),
        }

