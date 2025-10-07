# dirprojeto\aplicativo\forms\assunto03\forms.py
from django import forms
from aplicativo.models.assunto03.models import (
    TabelaSis1,
    TabelaSis2,
)

class TabelaSis1Form(forms.ModelForm):
    class Meta:
        model = TabelaSis1
        fields = '__all__'
        exclude = ['campo15','campo16']
        
        widgets = {
            'campo1': forms.TextInput(attrs={
                'placeholder': 'Campo de Texto Curto. CharField.',
                'class': 'form-control'
            }),
            'campo2': forms.Textarea(attrs={
                'placeholder': 'Campo de Texto Longo. TextField.',
                'class': 'form-control form-textarea',
                'rows': 4
            }),
            'campo3': forms.NumberInput(attrs={
                'placeholder': 'Número Inteiro. IntegerField.',
                'class': 'form-control'
            }),
            'campo4': forms.NumberInput(attrs={
                'placeholder': 'Número Decimal. FloatField.',
                'class': 'form-control',
                'step': '0.01'
            }),
            'campo5': forms.NumberInput(attrs={
                'placeholder': 'Número Decimal Precisão Fixa. DecimalField.',
                'class': 'form-control',
                'step': '0.01'
            }),
            'campo6': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'campo7': forms.DateInput(attrs={
                'placeholder': 'Data. DateField.',
                'type': 'date',
                'class': 'form-control'
            }),
            'campo8': forms.TimeInput(attrs={
                'placeholder': 'Hora. TimeField.',
                'type': 'time',
                'class': 'form-control'
            }),
            'campo9': forms.DateTimeInput(attrs={
                'placeholder': 'Data e Hora. DateTimeField.',
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'campo10': forms.EmailInput(attrs={
                'placeholder': 'E-mail. EmailField.',
                'class': 'form-control'
            }),
            'campo11': forms.URLInput(attrs={
                'placeholder': 'URL. URLField.',
                'class': 'form-control'
            }),
            'campo12': forms.TextInput(attrs={
                'placeholder': 'Slug. SlugField.',
                'class': 'form-control'
            }),
            'campo13': forms.TextInput(attrs={
                'placeholder': 'UUID. UUIDField.',
                'class': 'form-control'
            }),
            'campo14': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'campo17': forms.TextInput(attrs={
                'placeholder': 'Campo Único. Unique.',
                'class': 'form-control'
            }),
            'campo18': forms.NumberInput(attrs={
                'placeholder': 'Campo com Valor Padrão.',
                'class': 'form-control'
            }),
            'campo19': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
            'campo20': forms.NumberInput(attrs={
                'placeholder': 'Número Positivo.',
                'class': 'form-control',
                'min': '0'
            }),
            'campo21': forms.NumberInput(attrs={
                'placeholder': 'Número entre 0 e 100.',
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'step': '0.01'
            }),
            'Campo22': forms.Select(attrs={
                'class': 'form-control form-select'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes específicas para labels
        for field_name, field in self.fields.items():
            if field_name != 'campo6':  # Checkbox tem tratamento diferente
                field.widget.attrs.setdefault('class', 'form-control')
    
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
        fields = '__all__'
        
        widgets = {
            'campo1': forms.TextInput(attrs={
                'placeholder': 'Campo de Texto Curto. CharField.',
                'class': 'form-control'
            }),
            'campo2': forms.NumberInput(attrs={
                'placeholder': 'Número Inteiro. IntegerField.',
                'class': 'form-control'   
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.setdefault('class', 'form-control')
    
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
        
        fields = '__all__'
        widgets = {
            'campo1': forms.TextInput(attrs={
                'placeholder': 'placeholder. campo1: Campo de Texto Curto. CharField.',
                'class': 'form-control'
            }),
            'campo2': forms.NumberInput(attrs={
                'placeholder': 'placeholder. Número Inteiro. IntegerField.',
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