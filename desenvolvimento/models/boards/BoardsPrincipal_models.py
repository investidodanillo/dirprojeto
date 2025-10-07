# desenvolvimento\models\boards\BoardsPrincipal_models.py
from django.db import models
from django.contrib.auth.models import User
from desenvolvimento.models.boards.tabelas_boards_models import (
    Categoria,
    Sistema,
    TipoItem, 
    Prioridade, 
    Status)



class ItemEvolucao(models.Model):
    """
    Representa uma demanda de desenvolvimento:
    - Pode ser uma nova funcionalidade, bug, melhoria, documentação ou tarefa técnica.
    - Passa por diferentes status no ciclo de vida (pendente -> em andamento -> concluído).
    - Está sempre relacionado a um Sistema e, opcionalmente, a uma Categoria.
    """
    titulo = models.CharField(max_length=200) #texto
    descricao = models.TextField()            # texto
    tipo = models.CharField(max_length=10, choices=TipoItem.choices) # choices
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA) # choices
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE) # choices
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)   # FK
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # FK
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="itens_criados")  # FK
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="itens_responsavel")  # FK
    versao_prevista = models.CharField(max_length=20, blank=True, help_text="Ex: v1.2") # texto
    data_criacao = models.DateField(auto_now_add=True)
    atualizado_em = models.DateField(auto_now=True)
    data_conclusao = models.DateField(verbose_name="Data prevista", null=True, blank=True)

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.titulo}"


class Release(models.Model):
    """
    Representa uma versão de entrega de um sistema.
    Permite agrupar vários Itens de Evolução e documentar o que foi entregue.
    """
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    versao = models.CharField(max_length=20)  # Ex: v1.0.1
    descricao = models.TextField(blank=True)
    data = models.DateField(auto_now_add=True)
    itens = models.ManyToManyField(ItemEvolucao, blank=True)

    def __str__(self):
        return f"{self.sistema.nome} - {self.versao}"


class ChecklistSistema(models.Model):
    """
    Lista de verificação para garantir a qualidade de uma entrega/release.
    Ex: "Checklist de Publicação", "Checklist de Testes de Segurança".
    """
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sistema.nome} - {self.nome}"


class ChecklistItem(models.Model):
    """
    Item individual de um Checklist.
    Ex: "Rodar migrações", "Validar login", "Executar testes unitários".
    """
    checklist = models.ForeignKey(ChecklistSistema, on_delete=models.CASCADE, related_name="itens")
    descricao = models.CharField(max_length=200)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{'[OK]' if self.concluido else '[ ]'} {self.descricao}"
