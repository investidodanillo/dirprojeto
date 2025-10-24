# dirprojeto\aplicativo\models\assunto04\models.py
from django.db import models
from core.managers import TenantManager
from controles.models.empresas.Empresas_models import ControlesEmpresas 

class Produto(models.Model):
    Empresa = models.ForeignKey(ControlesEmpresas , on_delete=models.CASCADE, related_name="products")
    sku = models.CharField(max_length=100, verbose_name="SKY ")
    nome = models.CharField(max_length=100, verbose_name="NOME ")
    description = models.TextField(blank=True, null=True, verbose_name="DESCRIÇÃO ")
    quantity = models.DecimalField(max_digits=14, decimal_places=2, default=0, verbose_name="QUANTIDADE ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TenantManager()
    all_objects = models.Manager()

    class Meta:
        unique_together = ("Empresa", "nome")
        ordering = ["nome"]

    def __str__(self):
        return f"{self.name} ({self.Empresa})"