# core/models.py
from django.db import models
from .managers import TenantManager

class ModeloBaseTenant(models.Model):
    empresa = models.ForeignKey(
        'controles.Empresas',  # Use string para evitar import circular
        on_delete=models.CASCADE,
        editable=False
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    objects = TenantManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
