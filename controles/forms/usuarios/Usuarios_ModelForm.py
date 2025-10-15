# dirprojeto\controles\forms\usuarios\Usuarios_ModelForm.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    Formulário de registro completo de usuário, baseado no model User.
    Inclui campos administrativos como is_staff e is_active, apenas se necessário.
    """

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'is_staff',
            'is_active',
            'is_superuser',
            'last_login',
            'date_joined',
        ]

        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmar Senha',
            'is_staff': 'É membro da equipe?',
            'is_active': 'Usuário ativo?',
            'is_superuser': 'É superusuário?',
            'last_login': 'Último login',
            'date_joined': 'Data de cadastro',
        }

        help_texts = {
            'username': 'Obrigatório. Até 150 caracteres. Letras, dígitos e @/./+/-/_ apenas.',
            'first_name': 'Primeiro nome.',
            'last_name': 'Sobrenome.',
            'email': 'Informe um e-mail válido.',
            'is_staff': 'Permite acesso ao painel administrativo.',
            'is_active': 'Indica se o usuário está ativo.',
            'is_superuser': 'Tem todas as permissões do sistema.',
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
                'placeholder': 'Seu e-mail',
                'class': 'form-control'
            }),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'last_login': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
            'date_joined': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'readonly': True
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Campos de senha personalizados
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Crie uma senha'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })

        # Campos administrativos visíveis apenas para superusuário (opcional)
        for field in ['is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']:
            self.fields[field].required = False
            if field in ['last_login', 'date_joined']:
                self.fields[field].disabled = True