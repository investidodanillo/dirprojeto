# controles\models\empresas\Empresas_models.py
from django.db import models
from django.contrib.auth.models import User
from core.managers import TenantManager
from core.threadlocal import get_current_company_id
from core.threadlocal import set_current_company_id
from core.managers import TenantManager
from core.models import Company
from core.middleware import CompanySessionMiddleware

class ControlesEmpresas(models.Model):
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, verbose_name="NOME: ")
    cnpj = models.CharField(max_length=18, blank=True, null=True, verbose_name="CNPJ: ")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)


    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome
