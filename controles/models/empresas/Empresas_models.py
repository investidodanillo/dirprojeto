# controles\models\empresas\Empresas_models.py
from django.db import models

class Empresas(models.Model):
    nome = models.CharField(max_length=200, verbose_name="nome da empresa")
    cnpj = models.CharField(
        max_length=18,
        unique=True,
        verbose_name="14 dígitos com máscara (00.000.000/0000-00)"
    )
    data_criacao = models.DateField(verbose_name="Criado em", auto_now_add=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = 'empresas'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome
