# desenvolvimento\tables\BoardsPrinciap_tables.py
from django.urls import reverse
from django.utils.html import format_html
import django_tables2 as tables
from desenvolvimento.models.boards.BoardsPrincipal_models import ItemEvolucao, Release, ChecklistSistema, ChecklistItem


class BoardsPrincipal_ItemEvolucao_Tab(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com:
    - botão de edição estilo glass-button
    - ícones para booleanos ✓ / ✗
    Integrada com CSS de glassmorphism (tabela-form e glass-button).
    """
    id=tables.Column(verbose_name="ID")
    titulo = tables.Column(verbose_name="TÍTULO")
    #descricao = tables.Column(verbose_name="Descrição")
    tipo = tables.Column(verbose_name="TIPO")
    prioridade = tables.Column(verbose_name="PRIORIDADE")
    status = tables.Column(verbose_name="STATUS")
    sistema = tables.Column(verbose_name="SISTEMA")
    categoria = tables.Column(verbose_name="CATEGORIA")
    #criado_por = tables.Column(verbose_name="Criado")    
    versao_prevista = tables.Column(verbose_name="VERSÃO")
    data_criacao = tables.Column(verbose_name="CRIAÇÃO")
    #atualizado_em = tables.Column(verbose_name="Atualização")
    #data_conclusao = tables.Column(verbose_name="CONCLUSÃO")
    

    acao = tables.Column(empty_values=(), verbose_name="AÇÕES")

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        Redireciona para a view de update usando o namespace 'assunto02'.
        """

        url = reverse("boards:boardsPrincipal_ItemEvolucao_UpdateDelete_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        ) 
    def render_prioridade(self, value):
        """
        Renderiza a coluna PRIORIDADE com cores diferentes para cada nível.
        """
        if value == 'Baixa':
            return format_html('<p class="prioridade prioridade-baixa">Baixa</p>')
        elif value == 'Média':
            return format_html('<p class="prioridade prioridade-media">Média</p>')
        elif value == 'Alta':
            return format_html('<p class="prioridade prioridade-alta">Alta</p>')
        elif value == 'Crítica':
            return format_html('<p class="prioridade prioridade-critica">Crítica</p>')
        else:
            return format_html('<p class="prioridade prioridade-desconhecida">-</p>')

    class Meta:
        model = ItemEvolucao
        fields = ('id','titulo', 'tipo', 'prioridade', 'status', 'sistema', 'categoria',  'responsavel', 'versao_prevista', 'data_criacao')
        attrs = {"class": "table table-striped table-hover tabela-form","id": "ItemEvolucao"}
        sequence = ('id','titulo', 'tipo', 'prioridade', 'status', 'sistema', 'categoria',  'responsavel', 'versao_prevista', 'data_criacao' )

class BoardsPrincipal_Release_Tab(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    sistema = tables.Column(verbose_name="SISTEMA", orderable=True)
    versao = tables.Column(verbose_name="VERSÃO", orderable=True)
    descricao = tables.Column(verbose_name="DESCRIÇÃO", orderable=False)
    data = tables.Column(verbose_name="DATA", orderable=True)
    itens = tables.Column(verbose_name="ITENS", orderable=False)

    acao = tables.Column(empty_values=(), verbose_name="AÇÕES", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("boards:boardsPrincial_Release_UpdateDelete_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    class Meta:
        model = Release
        fields = ("id","sistema", "versao", "descricao", "data", "itens")
        attrs = {
            "class": "table table-striped table-hover tabela-form",
            "id": "Release"
        }
        sequence = ("id","sistema", "versao", "descricao", "data", "itens", "acao")

class BoardsPrincipal_ChecklistSistema_Tab(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    sistema = tables.Column(verbose_name="SISTEMA", orderable=True)
    nome = tables.Column(verbose_name="NOME", orderable=True)
    descricao = tables.Column(verbose_name="DESCRIÇÃO", orderable=False)
    ativo = tables.Column(verbose_name="ATIVO", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="AÇÕES", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("boards:boardsPrincipal_ChecklistSistema_UpdateDelete_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    def render_ativo(self, value):
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
        model = ChecklistSistema
        fields = ("id","sistema", "nome", "descricao", "ativo")
        attrs = {
            "class": "table table-striped table-hover tabela-form",
            "id": "ChecklistSistema"
        }
        sequence = ("id","sistema", "nome", "descricao", "ativo", "acao")

class BoardsPrincipal_ChecklistItem_Tab(tables.Table):
    """
    Tabela para exibir os registros de Tabela1 com design glassmorphism.
    """
    id = tables.Column(verbose_name="ID", orderable=True)
    checklist = tables.Column(verbose_name="CHECKLIST", orderable=True)
    descricao = tables.Column(verbose_name="DESCRIÇÃO", orderable=False)
    concluido = tables.Column(verbose_name="CONCLUÍDO", orderable=True)

    acao = tables.Column(empty_values=(), verbose_name="AÇÕES", orderable=False)

    def render_acao(self, record):
        """
        Renderiza o botão 'Editar' com classe glass-button.
        """
        url = reverse("boards:boardsPrincipal_ChecklistItem_UpdateDelete_View", args=[record.pk])
        return format_html(
            '<a href="{}" class="btn btn-warning btn-sm" title="Editar Registro">'
            '<i class="fas fa-edit"></i> Editar</a>',
            url
        )

    def render_concluido(self, value):
        """
        Renderiza ícone ✓ para True e ✗ para False.
        """
        if value:
            return format_html(
                '<span class="status-ativo" title="Concluído">✓ Concluído</span>'
            )
        return format_html(
            '<span class="status-inativo" title="Pendente">✗ Pendente</span>'
        )

    class Meta:
        model = ChecklistItem
        fields = ("id","checklist", "descricao", "concluido")
        attrs = {
            "class": "table table-striped table-hover tabela-form",
            "id": "ChecklistItem"
        }
        sequence = ("id","checklist", "descricao", "concluido", "acao")
