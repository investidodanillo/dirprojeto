#aplicativo\views\assunto04\assunto04_capitulo01_View.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from aplicativo.models.assunto04 import Produto
#from controles.models.empresas.Empresas_models import ControlesEmpresas
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from aplicativo.tables.assunto04_tables import ProdutoTable
from aplicativo.filters.assunto04_filters import ProdutoFilter
from aplicativo.forms.assunto04.forms import ProdutoForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from core.models import Company
from controles.models.products.models import Product
from controles.forms.companies.forms import CompanyForm
from django.contrib import messages



#@login_required
#def assunto04_index(request):
#    if request.method == "POST":
#        company_id = request.POST.get("company_id")
#        if company_id:
#            try:
#                company = Company.objects.get(pk=company_id)
#                request.session["company_id"] = company.id
#                messages.success(request, f"Empresa selecionada: {company.name}")
#                next_url = request.GET.get("next") or "assunto04:assunto04_index"
#                return redirect(next_url)
#            except Company.DoesNotExist:
#                messages.error(request, "Empresa inválida.")
#        else:
#            request.session.pop("company_id", None)
#            messages.success(request, "Empresa desmarcada.")
#    companies = Company.objects.all()
#    return render(request, "assunto04/index.html", {"companies": companies, "current": request.session.get("company_id")})
#







def assunto04_index(request):
    return render(request, 'assunto04/index.html')

def assunto04_capitulo01_inicio_views(request):
    return render(request, 'assunto04/capitulo01/titulos/inicio.html')




class assunto04_capitulo01_cadastro_View(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'assunto04/capitulo01/titulos/assunto04_cadastro.html'
    def get_success_url(self):
        return reverse('assunto04:assunto04_Capitulo01_Update', kwargs={'pk': self.object.pk})



# editar e deletar os dados da tabela abelaSis1
class assunto04_Capitulo01_Update_View(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'assunto04/capitulo01/titulos/assunto04_update_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Produto, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('assunto04:assunto04_Capitulo01_Update', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('assunto04:assunto04_capitulo01_visualizar_View'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('assunto04:assunto04_capitulo01_cadastro'))       

        return super().post(request, *args, **kwargs)



class assunto04_capitulo01_ProdutoListViewTab(SingleTableMixin, FilterView):
    model = Produto
    table_class = ProdutoTable
    template_name = "assunto04/capitulo01/titulos/assunto04_capitulo01_ProdutoTab.html"
    filterset_class = ProdutoFilter
    paginate_by = 10
   
        # Define a mensagem padrão
    mensagem = "mensagem: mensagem"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensagem"] = self.mensagem
        return context
   