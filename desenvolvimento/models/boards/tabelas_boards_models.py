from django.db import models


class Categoria(models.Model):
    """
    Classificação auxiliar para agrupar Itens de Evolução.
    Ex: Backend, Frontend, Banco de Dados, Performance.
    """
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome
class Sistema(models.Model):
    """
    Representa um sistema/aplicativo que será gerenciado.
    Ex: MOLDE, Contabilidade, RH, Financeiro.
    """
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class TipoItem(models.TextChoices):
    """
    Tipos de itens que podem ser criados no processo de desenvolvimento.
    """
    FEATURE = 'FEAT', 'Nova Funcionalidade'
    BUG = 'BUG', 'Correção de Bug'
    MELHORIA = 'IMPR', 'Melhoria'
    DOCUMENTACAO = 'DOCS', 'Documentação'
    TAREFA = 'TASK', 'Tarefa Técnica'


class Prioridade(models.TextChoices):
    """
    Define a urgência/impacto de um Item de Evolução.
    """
    BAIXA = 'BAIXA', 'Baixa'
    MEDIA = 'MEDIA', 'Média'
    ALTA = 'ALTA', 'Alta'
    CRITICA = 'CRIT', 'Crítica'


class Status(models.TextChoices):
    """
    Define em que estágio do ciclo de vida o Item de Evolução está.
    """
    PENDENTE = 'Pendente', 'Pendente'
    EM_ANDAMENTO = 'Andamento', 'Em Andamento'
    REVISAO = 'Revisão', 'Revisão'
    BLOQUEADO = 'Bloqueado', 'Bloqueado'
    CONCLUIDO = 'Concluído', 'Concluído'
    CANCELADO = 'Cancelado', 'Cancelado'
    PUBLICADO = 'Publicado', 'Publicado'
