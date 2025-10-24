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
    Empresa = tables.Column(verbose_name="EMPRESA", orderable=True)
    name = tables.Column(verbose_name="NOME", orderable=True)
    quantidade = tables.Column(verbose_name="QUANTIDADE", orderable=True)    

    acao = tables.Column(empty_values=(), verbose_name="AÇÕES", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("assunto04:assunto04_Capitulo01_Update", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    
    class Meta:
        model = Produto
        fields = ('id', 'Empresa', 'name', 'quantidade', 'acao')
        attrs = {
            "class": "table table-striped table-hover",
            "id": "tabela1"
        }
        sequence = ("id", "Empresa", "name", "quantidade", "acao")