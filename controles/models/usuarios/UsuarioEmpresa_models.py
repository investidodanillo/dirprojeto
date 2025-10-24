# ========================================
# SOLUÇÃO 2: CRIAR MODELO UsuarioEmpresa
# controles/models/usuarios/UsuarioEmpresa_models.py (NOVO ARQUIVO)
# ========================================

from django.db import models
from django.conf import settings

class UsuarioEmpresa(models.Model):
    """
    Relacionamento N:N entre usuários e empresas.
    Permite que um usuário trabalhe em múltiplas empresas.
    """
    PAPEIS = [
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('operador', 'Operador'),
        ('consultor', 'Consultor'),
    ]
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Usa o modelo de usuário configurado
        on_delete=models.CASCADE,
        related_name='vinculos_empresas'
    )
    empresa = models.ForeignKey(
        'controles.Empresas',
        on_delete=models.CASCADE,
        related_name='vinculos_usuarios'
    )
    papel = models.CharField(
        max_length=20,
        choices=PAPEIS,
        default='operador',
        verbose_name="Papel na Empresa"
    )
    ativo = models.BooleanField(
        default=True, 
        verbose_name="Vínculo Ativo"
    )
    data_vinculo = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Data de Vínculo"
    )
    
    class Meta:
        db_table = 'usuario_empresa'
        unique_together = ['usuario', 'empresa']
        verbose_name = 'Vínculo Usuário-Empresa'
        verbose_name_plural = 'Vínculos Usuário-Empresa'
        ordering = ['empresa__nome']
    
    def __str__(self):
        return f"{self.usuario.username} → {self.empresa.nome} ({self.get_papel_display()})"