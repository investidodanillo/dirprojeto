# dirprojeto\aplicativo\forms\assunto02\ModelForm.py
# dirprojeto/aplicativo/forms/assunto02/ModelForm.py
from django import forms
from controles.models.empresas.Empresas_models import Empresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Campo 1, texto curto'
            }),
            'cnpj': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Campo 2, texto curto'
            }),
            'data_criacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ativa': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),            
        }

