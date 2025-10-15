#-- aplicativo\tables\assunto02_tables.py

from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables
from aplicativo.models.assunto04.models import(
    Produto,
)


class ProdutoTable(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    nome = tables.Column(verbose_name="Nome do Campo 1", orderable=True)
    descricao = tables.Column(verbose_name="Slug / Campo 2", orderable=True)
    quantidade = tables.Column(verbose_name="Confirmação", orderable=True)
    preco = tables.Column(verbose_name="Status", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="Ações", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("assunto04:assunto04_capitulo01_cadastro", args=[record.pk])
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
        model = Produto
        fields = ("id","campo1", "campo2", "campo3", "campo4")
        attrs = {
            "class": "table table-striped table-hover",
            "id": "tabela1"
        }
        sequence = ("id", "campo1", "campo2", "campo3", "campo4", "acao")