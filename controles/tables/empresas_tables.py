#-- aplicativo\tables\assunto02_tables.py

from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables
from controles.models.empresas.Empresas_models import ControlesEmpresas


class EmpresasTable(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    nome = tables.Column(verbose_name="Nome", orderable=True)
    cnpj = tables.Column(verbose_name="CNPJ", orderable=True)
    data_criacao = tables.Column(verbose_name="Criação", orderable=True)
    created_at = tables.DateTimeColumn(verbose_name="Data de Criação", format="d/m/Y H:i", orderable=True)
    ativa = tables.Column(verbose_name="Status", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="Ações", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("empresas:controles_empresas_Update", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    def render_ativa(self, value):
        """
        Renderiza ícone ✓ para True e ✗ para False.
        """
        if value:
            return format_html(
                '<span class="status-ativo" title="Ativo">✓ Ativo</span>'
            )
        return format_html(
            '<span class="status-inativo" title="Inativo">✗ Inativo</span>'
        )    

    class Meta:
        model = ControlesEmpresas
        fields = ("id","nome", "cnpj", "data_criacao", "ativa")
        attrs = {
            "class": "table table-striped table-hover",
            "id": "tabela1"
        }
        sequence = ("id","nome", "cnpj", "data_criacao", "ativa")