#dirprojeto\aplicativo\views\assunto02\assunto02_capitulo01_View.py
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from aplicativo.models.assunto02 import Tabela1
from aplicativo.forms.assunto02.ModelForm import Tabela1Form
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from aplicativo.filters.assunto02_filters import Tabela1Filter
from aplicativo.tables.assunto02_tables import Tables1

def assunto02_index_View(request):
    return render(request, 'assunto02/index.html')

def assunto02_capitulo01_View_inicio(request):
    return render(request, 'assunto02/capitulo01/titulos/inicio.html')

#
class assunto02_capitulo01_cadastro_View(CreateView):
    model = Tabela1
    form_class = Tabela1Form
    template_name = 'assunto02/capitulo01/titulos/assunto02_cadastro.html'
    def get_success_url(self):
        return reverse('assunto02:assunto02_Capitulo01_Update_View', kwargs={'pk': self.object.pk})



# #essa view é para editar e deletar os dados da tabela
class assunto02_Capitulo01_Update_View(UpdateView):
    model = Tabela1
    form_class = Tabela1Form
    template_name = 'assunto02/capitulo01/titulos/assunto02_update_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Tabela1, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('assunto02:assunto02_Capitulo01_Update_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('assunto02:assunto02_capitulo01_visualizar_View'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('assunto02:assunto02_capitulo01_cadastro_View'))       

        return super().post(request, *args, **kwargs)


#essa view é para visualizar os dados da tabela    
class assunto02_capitulo01_visualizar_View(ListView):
    model = Tabela1
    template_name = 'assunto02/capitulo01/titulos/assunto02_visualizar.html'
    paginate_by = 20
    context_object_name = 'tabela1_list'  # Nome do contexto para a lista de objetos

    def get_queryset(self):
        return Tabela1.objects.all()  # Retorna todos os objetos da tabela Tabela1
    
#
class assunto02_capitulo01_Tabela1ListView(SingleTableMixin, FilterView):
    model = Tabela1
    table_class = Tables1
    template_name = "assunto02/capitulo01/titulos/assunto02_capitulo01_Tabela1.html"
    filterset_class = Tabela1Filter
    paginate_by = 10
   
        # Define a mensagem padrão
    mensagem = "mensagem: mensagem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = self.mensagem
        return context
    