# dirprojeto\aplicativo\forms\assunto02\ModelForm.py
from django import forms
from aplicativo.models.assunto02.models import Tabela1

class Tabela1Form(forms.ModelForm):
    class Meta:
        model = Tabela1
        fields = '__all__'
        widgets = {
            'campo1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 1, texto curto'}),
            'campo2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Campo 2, texto curto'}),
            'campo3': forms.Select(choices=Tabela1.CONFIRMA, attrs={'class': 'form-control', 'placeholder': 'Campo 3, escolha'}),
            'campo4': forms.CheckboxInput(attrs={'class': 'form-check-input', 'placeholder': 'Campo 4, checkbox'}),
            'campo5': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Campo 5, texto longo'}),
            

        }
