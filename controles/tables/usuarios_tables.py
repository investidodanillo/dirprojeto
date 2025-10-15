#-controles\tables\usuarios_tables.py

from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables
from django.contrib.auth.models import User


class UsuariosTable(tables.Table):
    id = tables.Column(verbose_name="ID", orderable=True)
    username = tables.Column(verbose_name="Usuário", orderable=True)
    first_name = tables.Column(verbose_name="Nome", orderable=True)
    last_name = tables.Column(verbose_name="Sobrenome", orderable=True)
    email = tables.Column(verbose_name="Email", orderable=True)
    is_active = tables.BooleanColumn(verbose_name="Ativo", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="Ações", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("usuarios:controles_usuarios_Update_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    # ✅ Exemplo de renderizador booleano
    def render_is_active(self, value):
        """
        Renderiza ícone ✓ para True e ✗ para False (campo padrão do User).
        """
        if value:
            return format_html('<span class="status-ativo" title="Ativo">✓ Ativo</span>')
        return format_html('<span class="status-inativo" title="Inativo">✗ Inativo</span>')    

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_active")
        attrs = {
            "class": "table table-striped table-hover",
            "id": "tabela_usuarios"
        }
        sequence = ("id", "username", "first_name", "last_name", "email", "is_active", "acao")
        per_page = 10  # Paginação: 10 registros por página
        order_by = "-is_active"  # Ordenação padrão: mais recentes primeiro


