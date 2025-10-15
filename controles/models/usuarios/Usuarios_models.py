# dirprojeto\aplicativo\models\assunto02\models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    empresa = models.ForeignKey(
        'empresas.Empresa',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Empresa vinculada"
    )
    telefone = models.CharField(max_length=20, blank=True)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f"{self.username} - {self.empresa.nome if self.empresa else 'Sem empresa'}"

