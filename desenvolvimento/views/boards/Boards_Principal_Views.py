#dirprojeto\aplicativo\views\assunto03\assunto03_capitulo01_View.py
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from desenvolvimento.models.boards.BoardsPrincipal_models import ItemEvolucao, Release, ChecklistSistema, ChecklistItem
from desenvolvimento.models.boards.tabelas_boards_models import Status
from desenvolvimento.forms.boards.boards_forms import ItemEvolucaoForm, ReleaseForm, ChecklistSistemaForm, ChecklistItemForm
from desenvolvimento.tables.BoardsPrinciap_tables import BoardsPrincipal_ItemEvolucao_Tab, BoardsPrincipal_ChecklistSistema_Tab, BoardsPrincipal_ChecklistItem_Tab, BoardsPrincipal_Release_Tab

from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from desenvolvimento.filters.BoardsPrincipal_filters import BoardsPrincipal_ItemEvolucao_Filter, BoardsPrincipal_ChecklistSistema_Filter, BoardsPrincipal_ChecklistItem_Filter, BoardsPrincipal_Release_Filter

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect



def boards_principal_index_Views(request):
    return render(request, 'boards/index.html')

def boards_principal_inicio_Views(request):
    return render(request, 'boards/principal/titulos/inicio.html')
#==============================================================================================
# BOARDS QUADRO
def BoardsPrincial_kanban_view(request):
    """
    View pública para exibir o Kanban com os itens de evolução organizados por status
    """
    # Filtra os itens conforme necessário (ex: por sistema, usuário, etc.)
    # Aqui estamos trazendo todos os itens, mas você pode ajustar o filtro
    itens = ItemEvolucao.objects.all().select_related('responsavel', 'sistema', 'categoria')
    
    # Organiza os itens por status
    pendente = itens.filter(status=Status.PENDENTE)
    andamento = itens.filter(status=Status.EM_ANDAMENTO)
    revisao = itens.filter(status=Status.REVISAO)
    concluido = itens.filter(status=Status.CONCLUIDO)
    
    context = {
        'pendente': pendente,
        'pendente_count': pendente.count(),
        'andamento': andamento,
        'andamento_count': andamento.count(),
        'revisao': revisao,
        'revisao_count': revisao.count(),
        'concluido': concluido,
        'concluido_count': concluido.count(),
    }
    
    return render(request, 'boards/principal/titulos/BoardsPrincial_Quadro.html', context)

#==============================================================================================
# ITEM EVOLUÇÃO
# cadastro ItemEvolucao
class BoardsPrincipal_ItemEvolucao_cadastro_View(CreateView):
    model = ItemEvolucao
    form_class = ItemEvolucaoForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_ItemEvolucao_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ItemEvolucao_UpdateDelete_View', kwargs={'pk': self.object.pk})

# UpdateDelete ItemEvolucao    
class BoardsPrincipal_ItemEvolucao_UpdateDelete_View(UpdateView):
    model = ItemEvolucao
    form_class = ItemEvolucaoForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_ItemEvolucao_UpdateDelete.html'
    def get_object(self, queryset=None):
        return get_object_or_404(ItemEvolucao, pk=self.kwargs.get("pk"))
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ItemEvolucao_UpdateDelete_View', kwargs={'pk': self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")
        if action == "salvar":
            return super().post(request, *args, **kwargs)
        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:BoardsPrincipal_ItemEvolucao_TabListView'))
        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:boardsPrincipal_ItemEvolucao_cadastro_View'))
        return super().post(request, *args, **kwargs)

# Visualizar ItemEvolucao  Tabela
class BoardsPrincipal_ItemEvolucao_TabListView(SingleTableMixin, FilterView):
    model = ItemEvolucao
    table_class = BoardsPrincipal_ItemEvolucao_Tab
    template_name = "boards/principal/titulos/BoardsPrincipal_ItemEvolucao_Table.html"
    filterset_class = BoardsPrincipal_ItemEvolucao_Filter
    paginate_by = 10

#==============================================================================================
#RELEASE
#cadastro de   Release
class BoardsPrincipal_Release_cadastro_View(CreateView):
    model = Release
    form_class = ReleaseForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_Release_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsPrincial_Release_UpdateDelete_View', kwargs={'pk': self.object.pk})
# UpdateDelete Release
class BoardsPrincial_Release_UpdateDelete_View(UpdateView):
    model = Release
    form_class = ReleaseForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_Release_UpdateDelete.html'
    def get_object(self, queryset=None):
        return get_object_or_404(Release, pk=self.kwargs.get("pk"))
    def get_success_url(self):
        return reverse('boards:boardsPrincial_Release_UpdateDelete_View', kwargs={'pk': self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")
        if action == "salvar":
            return super().post(request, *args, **kwargs)
        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:boardsPrincipal_Release_visualizar_View'))
        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:boardsPrincipal_Release_visualizar_View'))
        return super().post(request, *args, **kwargs)
    
# visualizar Release
class BoardsPrincipal_Release_TabListView(SingleTableMixin, FilterView):
    model = Release
    table_class = BoardsPrincipal_Release_Tab
    template_name = "boards/principal/titulos/BoardsPrincipal_Release_Table.html"
    filterset_class = BoardsPrincipal_Release_Filter
    paginate_by = 10   

#==============================================================================================
# CHECKLIST SISTEMA
# cadastro ChecklistSistema
class BoardsPrincipal_ChecklistSistema_cadastro_View(CreateView):
    model = ChecklistSistema
    form_class = ChecklistSistemaForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_ChecklistSistema_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ChecklistSistema_UpdateDelete_View', kwargs={'pk': self.object.pk})

#visualizar ChecklistSistema em tabela
class BoardsPrincipal_ChecklistSistema_TabListView(SingleTableMixin, FilterView):
    model = ChecklistSistema
    table_class = BoardsPrincipal_ChecklistSistema_Tab
    template_name = "boards/principal/titulos/BoardsPrincipal_ChecklistSistema_Table.html"
    filterset_class = BoardsPrincipal_ChecklistSistema_Filter
    paginate_by = 10


# UpdateDelete ChecklistSistema
class BoardsPrincipal_ChecklistSistema_UpdateDelete_View(UpdateView):
    model = ChecklistSistema
    form_class = ChecklistSistemaForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_ChecklistSistema_UpdateDelete.html'
    def get_object(self, queryset=None):
        return get_object_or_404(ChecklistSistema, pk=self.kwargs.get("pk"))
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ChecklistSistema_UpdateDelete_View', kwargs={'pk': self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")
        if action == "salvar":
            return super().post(request, *args, **kwargs)
        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:oardsPrincipal_ChecklistSistema_visualizar_View'))
        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:oardsPrincipal_ChecklistSistema_visualizar_View'))
        return super().post(request, *args, **kwargs)   
#==============================================================================================
# CHECKLIST ITEM
# cadastro ChecklistItem
class BoardsPrincipal_ChecklistItem_cadastro_View(CreateView):
    model = ChecklistItem
    form_class = ChecklistItemForm
    template_name = 'boards/principal/titulos/BoardsPrincipal_ChecklistItem_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ChecklistItem_UpdateDelete_View', kwargs={'pk': self.object.pk})
# UpdateDelete ChecklistItem
class BoardsPrincipal_ChecklistItem_UpdateDelete_View(UpdateView):
    model = ChecklistItem
    form_class = ChecklistItemForm
    template_name = 'boards/principal/titulos/boardsPrincipal_ChecklistItem_UpdateDelete_View.html'
    def get_object(self, queryset=None):
        return get_object_or_404(ChecklistItem, pk=self.kwargs.get("pk"))
    def get_success_url(self):
        return reverse('boards:boardsPrincipal_ChecklistItem_UpdateDelete_View', kwargs={'pk': self.object.pk})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")
        if action == "salvar":
            return super().post(request, *args, **kwargs)
        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:boardsPrincipal_ChecklistItem_visualizar_View'))
        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:boardsPrincipal_ChecklistItem_visualizar_View'))   
        return super().post(request, *args, **kwargs)    
# visualizar ChecklistItem    
class BoardsPrincipal_ChecklistItem_TabListView(SingleTableMixin, FilterView):
    model = ChecklistItem
    table_class = BoardsPrincipal_ChecklistItem_Tab
    template_name = "boards/principal/titulos/BoardsPrincipal_ChecklistItem_Table.html"
    filterset_class = BoardsPrincipal_ChecklistItem_Filter
    paginate_by = 10