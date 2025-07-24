#dirprojeto\aplicativo\forms\assunto03\forms.py
from django import forms
from aplicativo.models.assunto03.models import (
    TabelaSis1,
    TabelaSis2,
    )

class TabelaSis1Form(forms.ModelForm):
    class Meta:
        model = TabelaSis1
        # Liste apenas os campos que deseja exibir no formulário
        fields = '__all__'
        exclude = ['campo15','campo16']
        campo22 = forms.ModelChoiceField(queryset=TabelaSis2.objects.all())
        widgets = {
            'campo1': forms.TextInput(attrs={
                'placeholder': 'placeholder. campo1: Campo de Texto Curto. CharField.',
                'class': 'glass-input-text'
            }),
            'campo2': forms.Textarea(attrs={
                'placeholder': 'placeholder. Campo de Texto Longo. TextField.',
                'class': 'glass-input-textarea'
            }),
            'campo3': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Inteiro. IntegerField.',
                'class': 'glass-input-number'
            }),
            'campo4': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Decimal. FloatField.',
                'class': 'glass-input-float'
            }),
            'campo5': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Decimal Precisão Fixa. DecimalField.',
                'class': 'glass-input-decimal'
            }),
            'campo6': forms.CheckboxInput(attrs={
                'class': 'glass-input-checkbox'
            }),
            'campo7': forms.DateInput(attrs={
                'placeholder': 'placeholder. Data. DateField.',
                'type': 'date',
                'class': 'glass-input-date'
            }),
            'campo8': forms.TimeInput(attrs={
                'placeholder': 'placeholder. Hora. TimeField.',
                'type': 'time',
                'class': 'glass-input-time'
            }),
            'campo9': forms.DateTimeInput(attrs={
                'placeholder': 'placeholder. Data e Hora. DateTimeField.',
                'type': 'datetime-local',
                'class': 'glass-input-datetime'
            }),
            'campo10': forms.EmailInput(attrs={
                'placeholder': 'placeholder. E-mail. EmailField.',
                'class': 'glass-input-email'
            }),
            'campo11': forms.URLInput(attrs={
                'placeholder': 'placeholder. URL. URLField.',
                'class': 'glass-input-url'
            }),
            'campo14': forms.ClearableFileInput(attrs={
                'class': 'glass-input-file'
            }),
            'campo17': forms.TextInput(attrs={
                'placeholder': 'placeholder. Campo Único. Unique.',
                'class': 'glass-input-unique'
            }),
            'campo18': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Campo com Valor Padrão.',
                'class': 'glass-input-default'
            }),
            'campo19': forms.Select(attrs={
                'placeholder': 'placeholder. Campo com Choices.',
                'class': 'glass-input-select'
            }),
            'campo20': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Positivo.',
                'class': 'glass-input-positive'
            }),
            'campo21': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número entre 0 e 100.',
                'class': 'glass-input-range'
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

class TabelaSis2Form(forms.ModelForm):
    class Meta:
        model = TabelaSis2
        # Liste apenas os campos que deseja exibir no formulário
        fields = '__all__'
        widgets = {
            'campo1': forms.TextInput(attrs={
                'placeholder': 'placeholder. campo1: Campo de Texto Curto. CharField.',
                'class': 'glass-input-text'
            }),
            'campo2': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Inteiro. IntegerField.',
                'class': 'glass-input-number'   
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