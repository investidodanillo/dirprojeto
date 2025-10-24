# dirprojeto/aplicativo/forms/assunto02/ModelForm.py
from django import forms
from controles.models.empresas.Empresas_models import ControlesEmpresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = ControlesEmpresas
        fields = '__all__'
        exclude = ['created_by', 'created_at']
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'nome da empresa.',
                'class': 'form-control'
            }),

            'cnpj': forms.NumberInput(attrs={
                'placeholder': 'CNPJ da empresa, 14 dígitos.',
                'class': 'form-control'
            }),
            'ativa': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),            
        }

