# dirprojeto\controles\forms\usuarios\Usuarios_ModelForm.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# dirprojeto\controles\forms\usuarios\Usuarios_ModelForm.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # Remova as declarações explícitas dos campos ou ajuste-as
    # Mantenha apenas campos personalizados se necessário
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
        }
        
        help_texts = {
            'username': 'Obrigatório. Até 150 caracteres. Letras, dígitos e @/./+/-/_ apenas.',
            'first_name': 'Obrigatório. Primeiro nome.',
            'last_name': 'Obrigatório. Sobrenome.',
            'email': 'Obrigatório. Informe um e-mail válido.',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Escolha um nome de usuário',
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Seu primeiro nome',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Seu sobrenome',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Seu endereço de e-mail',
                'class': 'form-control'
            }),
            # password1 e password2 são tratados pelo UserCreationForm
        }
    
    # Adicione estilização para os campos de senha
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Crie uma senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })