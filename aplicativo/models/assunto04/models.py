# dirprojeto\aplicativo\models\assunto04\models.py
from django.db import models
from core.models import ModeloBaseTenant

class Produto(ModeloBaseTenant):
    nome = models.CharField(max_length=100, verbose_name="NOME DO PRODUTO")
    descricao = models.TextField(verbose_name="DESCRIÇÃO DO PRODUTO")
    quantidade = models.IntegerField(verbose_name="QUANTIDADE DO PRODUTO")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="PREÇO DO PRODUTO")
    def __str__(self):
        return self.nome

