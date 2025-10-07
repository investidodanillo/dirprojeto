#-- aplicativo\tables\assunto02_tables.py

from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables
from aplicativo.models.assunto02.models import Tabela1


class Tables1(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    campo1 = tables.Column(verbose_name="Nome do Campo 1", orderable=True)
    campo2 = tables.Column(verbose_name="Slug / Campo 2", orderable=True)
    campo3 = tables.Column(verbose_name="Confirmação", orderable=True)
    campo4 = tables.Column(verbose_name="Status", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="Ações", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("assunto02:assunto02_Capitulo01_Update_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    def render_campo4(self, value):
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

    def render_campo3(self, value):
        """
        Melhora a exibição do campo de confirmação.
        """
        if value == 'S':
            return format_html('<span class="status-confirmado">Confirmado</span>')
        elif value == 'N':
            return format_html('<span class="status-inativo">Negado</span>')
        else:
            return format_html('<span class="status-pendente">Pendente</span>')

    class Meta:
        model = Tabela1
        fields = ("id","campo1", "campo2", "campo3", "campo4")
        attrs = {
            "class": "table table-striped table-hover",
            "id": "tabela1"
        }
        sequence = ("id", "campo1", "campo2", "campo3", "campo4", "acao")