#dirprojeto\aplicativo\views\assunto03\assunto03_capitulo01_View.py
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from desenvolvimento.models.boards.tabelas_boards_models import(
    Categoria,
    Sistema,
  )
from desenvolvimento.forms.boards.tabelas_forms import CategoriaForm, SistemaForm

#from desenvolvimento.forms import Boards_Tabela1Form


def boards_tabelas_index_Views(request):
    return render(request, 'boards/index.html')

def boards_tabelas_inicio_Views(request):
    return render(request, 'boards/boards_tabelas/titulos/inicio.html')
#===================================================================================================================
#CATEGORIA
class BoardsTabelas_Categoria_cadastro_Views(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Categoria_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsTabelas_Categoria_UpdateDelete_View', kwargs={'pk': self.object.pk})
    

# #essa view é para editar e deletar os dados da tabela
class BoardsTabelas_Categoria_UpdateDelete_View(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Categoria_UpdateDelete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Categoria, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('boards:boardsTabelas_Categoria_UpdateDelete_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:boards_tabelas_visualizar_Views'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:boards_tabelas_cadastro_Views'))       

        return super().post(request, *args, **kwargs)
    
#essa view é para visualizar os dados da tabela    
class BoardsTabelas_Categoria_visualizar_View(ListView):
    model = Categoria
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Categoria_visualizar.html'
    paginate_by = 20
    context_object_name = 'Categoria_list'  # Nome do contexto para a lista de objetos

    def get_queryset(self):
        return Categoria.objects.all()  # Retorna todos os objetos da tabela Tabela1
    
#===================================================================================================================
# Sistema
class BoardsTabelas_Sistemas_cadastro_View(CreateView):
    model = Sistema
    form_class = SistemaForm
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Sistemas_cadastro.html'
    def get_success_url(self):
        return reverse('boards:boardsTabelas_Sistemas_UpdateDelete_View', kwargs={'pk': self.object.pk})
    
# #essa view é para editar e deletar os dados da tabela
class BoardsTabelas_Sistemas_UpdateDelete_View(UpdateView):
    model = Sistema
    form_class = SistemaForm
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Sistemas_UpdateDelete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Sistema, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('boards:boardsTabelas_Sistemas_UpdateDelete_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('boards:boardsTabelas_Sistemas_visualizar_View'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('boards:boardsTabelas_Sistemas_cadastro_Views'))       

        return super().post(request, *args, **kwargs)
        
class BoardsTabelas_Sistemas_visualizar_View(ListView):
    model = Sistema
    template_name = 'boards/boards_tabelas/titulos/BoardsTabelas_Sistemas_visualizar.html'
    paginate_by = 20
    context_object_name = 'Sistema_list'  # Nome do contexto para a lista de objetos

    def get_queryset(self):
        return Sistema.objects.all()  # Retorna todos os objetos da tabela Tabela1