# dirprojeto\aplicativo\models\assunto04\models.py
from django.db import models
#from core.models import ModeloBaseTenant

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="campo1: Campo de Texto Curto")
    descricao = models.TextField(verbose_name="campo2: Campo de Texto Longo")
    quantidade = models.IntegerField(verbose_name="campo3: Número Inteiro")
    preco = models.DecimalField(max_digits=10, decimal_places=2)    
    def __str__(self):
        return self.nome
