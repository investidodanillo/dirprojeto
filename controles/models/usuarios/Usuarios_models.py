# dirprojeto\aplicativo\models\assunto02\models.py
# ========================================
# SOLUÇÃO 1: CORRIGIR O MODELO Usuario
# controles/models/usuarios/Usuarios_models.py
# ========================================
#
#from django.db import models
#from django.contrib.auth.models import AbstractUser
#
#class Usuario(AbstractUser):
#    """
#    REMOVIDO: campo 'empresa' único
#    ADICIONADO: campo 'empresa_padrao' (opcional)
#    """
#    empresa_padrao = models.ForeignKey(
#        'controles.Empresas',  # Corrigido: era 'empresas.Empresa', agora é 'controles.Empresas'
#        on_delete=models.SET_NULL,
#        null=True,
#        blank=True,
#        verbose_name="Empresa Padrão",
#        help_text="Empresa usada automaticamente no login"
#    )
#    telefone = models.CharField(max_length=20, blank=True)
#    
#    class Meta:
#        db_table = 'usuarios'
#        verbose_name = 'Usuário'
#        verbose_name_plural = 'Usuários'
#
#    def __str__(self):
#        return f"{self.username}"
#    
#    def get_empresas_disponiveis(self):
#        """Retorna empresas que o usuário tem acesso."""
#        return self.vinculos_empresas.filter(
#            ativo=True,
#            empresa__ativa=True
#        ).select_related('empresa')
#    
#    def pode_acessar_empresa(self, empresa_id):
#        """Verifica se usuário pode acessar determinada empresa."""
#        return self.vinculos_empresas.filter(
#            empresa_id=empresa_id,
#            ativo=True,
#            empresa__ativa=True
#        ).exists()
#