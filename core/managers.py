# core/managers.py
from django.db import models
from .threadlocal import get_current_empresa  # Use threadlocal, não utils

class TenantManager(models.Manager):
    def get_queryset(self):
        empresa = get_current_empresa()
        if empresa is None:
            # Em vez de retornar none, você pode querer levantar uma exceção
            # ou retornar um queryset vazio
            return super().get_queryset().none()
        return super().get_queryset().filter(empresa=empresa)
"""
class LancamentoContabil(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	# ... outros campos
	objects = TenantManager() # Manager principal: filtra por empresa automaticamente
	all_objects = models.Manager() # Acesso sem filtro (use apenas para admin ou manutenção)
    
    """