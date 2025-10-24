# dirprojeto\aplicativo\forms\assunto02\ModelForm.py
from django import forms
from aplicativo.models.assunto04.models import (
    Produto,
     )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        
        
        widgets = {
            'Empresa': forms.Select(attrs={
                'placeholder': 'Selecione a Empresa.',
                'class': 'form-control form-select'              
            }),

            'sku': forms.TextInput(attrs={
                'placeholder': 'SKU do Produto. CharField.',
                'class': 'form-control form-textarea',
                'rows': 4
            }),
            'nome': forms.TextInput(attrs={
                'placeholder': 'Campo de Texto Curto. CharField.',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descrição do Produto. TextField.',
                'class': 'form-control form-textarea',
                'rows': 4
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantidade do Produto. DecimalField.',
                'class': 'form-control'
            }),            
        }       
    def form_valid(self, form):
        if form.is_valid():
            print("Formulário válido")
            return super().form_valid(form)
        else:
            print("Formulário inválido")
            print(form.errors)
            return self.form_invalid(form)