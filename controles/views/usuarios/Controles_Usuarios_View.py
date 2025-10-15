# dirprojeto\controles\views\Controles_Index\Controles_Usuarios_View.py
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from controles.forms.usuarios.Usuarios_ModelForm import UserRegisterForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from controles.filters.usuarios_filters import UsuariosFilter
from controles.tables.usuarios_tables import UsuariosTable




def controles_usuarios_View_index(request):
    return render(request, 'usuarios/index.html')

def controles_usuarios_View_inicio(request):
    return render(request, 'usuarios/titulos/inicio.html')

# cadastro de usuarios
class controles_usuarios_cadastro_View(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'usuarios/titulos/usuarios_cadastro.html'
    def get_success_url(self):
        return reverse('usuarios:assunto02_Capitulo01_Update_View', kwargs={'pk': self.object.pk})



# #essa view é para editar e deletar os dados da tabela
class controles_usuarios_Update_View(UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'usuarios/titulos/usuarios_update_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('usuarios:controles_usuarios_Update_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('usuarios:Controles_Usuarios_ListViewTab'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('usuarios:controles_usuarios_cadastro_View'))       

        return super().post(request, *args, **kwargs)


#essa view é para visualizar os dados da tabela User
# controles\views\usuarios\Controles_Usuarios_View.py  

class Controles_Usuarios_ListViewTab(SingleTableMixin, FilterView):
    """
    View que exibe os usuários com tabela e filtros.
    """
    model = User
    table_class = UsuariosTable
    template_name = "usuarios/titulos/usuarios_VisualizarTab.html"
    filterset_class = UsuariosFilter
    paginate_by = 10

    mensagem = "mensagem: mensagem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = self.mensagem
        return context
    