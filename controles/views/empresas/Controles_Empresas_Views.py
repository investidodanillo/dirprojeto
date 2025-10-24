# dirprojeto\controles\views\Controles_Index\Controles_empresas_View.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from controles.forms.empresas.Empresas_ModelForm import EmpresasForm
from controles.models.empresas.Empresas_models import ControlesEmpresas
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django_filters.views import FilterView
from controles.filters.empresas_filters import EmpresasFilter
from controles.tables.empresas_tables import EmpresasTable
from django_tables2.views import SingleTableMixin


from django.contrib.auth.decorators import login_required

#
#
def controles_empresas_View_index(request):
    return render(request, 'empresas/index.html')

def controles_empresas_View_inicio(request):
    return render(request, 'empresas/titulos/empresas_inicio.html')

# cadastro de empresas
class controles_empresas_cadastro_View(CreateView):
    model = ControlesEmpresas
    form_class = EmpresasForm
    template_name = 'empresas/titulos/empresas_cadastro.html'
    def get_success_url(self):
        return reverse('empresas:controles_empresas_Update', kwargs={'pk': self.object.pk})

# #essa view é para editar e deletar os dados da tabela
class controles_empresas_Update_View(UpdateView):
    model = ControlesEmpresas
    form_class = EmpresasForm
    template_name = 'empresas/titulos/empresas_update_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(ControlesEmpresas, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('empresas:controles_empresas_Update', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('empresas:Controles_empresas_ListViewTab'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('empresas:controles_empresas_cadastro'))       

        return super().post(request, *args, **kwargs)


#essa view é para visualizar os dados da tabela User
class Controles_empresas_ListViewTab(SingleTableMixin, FilterView):
    """
    View que exibe os usuários com tabela e filtros.
    """
    model = ControlesEmpresas
    table_class = EmpresasTable
    template_name = "empresas/titulos/empresas_visualizarTab.html"
    filterset_class = EmpresasFilter
    paginate_by = 10

    mensagem = "mensagem: mensagem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = self.mensagem
        return context
    