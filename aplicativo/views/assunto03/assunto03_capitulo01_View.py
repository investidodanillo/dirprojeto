#dirprojeto\aplicativo\views\assunto03\assunto03_capitulo01_View.py
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from aplicativo.models.assunto03 import TabelaSis1, TabelaSis2
from aplicativo.forms.assunto03.forms import TabelaSis1Form, TabelaSis2Form
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def assunto03_index_View(request):
    return render(request, 'assunto03/index.html')

def assunto03_capitulo01_View_inicio(request):
    return render(request, 'assunto03/capitulo01/titulos/inicio.html')

# CADASTRO abelaSis1
class assunto03_capitulo01_cadastro_View(CreateView):
    model = TabelaSis1
    form_class = TabelaSis1Form
    template_name = 'assunto03/capitulo01/titulos/assunto03_cadastro.html'
    def get_success_url(self):
        return reverse('assunto03:assunto03_Capitulo01_Update_View', kwargs={'pk': self.object.pk})



# editar e deletar os dados da tabela abelaSis1
class assunto03_Capitulo01_Update_View(UpdateView):
    model = TabelaSis1
    form_class = TabelaSis1Form
    template_name = 'assunto03/capitulo01/titulos/assunto03_update_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(TabelaSis1, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('assunto03:assunto03_Capitulo01_Update_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('assunto03:assunto03_capitulo01_visualizar_View'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('assunto03:assunto03_capitulo01_cadastro_View'))       

        return super().post(request, *args, **kwargs)

#essa view é para visualizar os dados da tabela    
class assunto03_capitulo01_visualizar_View(ListView):
    model = TabelaSis1
    template_name = 'assunto03/capitulo01/titulos/assunto03_visualizar.html'
    paginate_by = 20
    context_object_name = 'TabelaSis1_list'  

    def get_queryset(self):
        return TabelaSis1.objects.all()  



#===================================================================================================================
# CADASTRO TabelaSis2
class assunto03_capitulo01_cadastro_TabelaSis2_View(CreateView):
    model = TabelaSis2
    form_class = TabelaSis2Form
    template_name = 'assunto03/capitulo01/titulos/assunto03_cadastro2.html'

    def get_success_url(self):
        return reverse('assunto03:assunto03_Capitulo01_Update2_View', kwargs={'pk': self.object.pk})
    
# editar e deletar os dados da tabela abelaSis2
class assunto03_Capitulo01_Update2_View(UpdateView):
    model = TabelaSis2
    form_class = TabelaSis2Form
    template_name = 'assunto03/capitulo01/titulos/assunto03_update_delete2.html'

    def get_object(self, queryset=None):
        return get_object_or_404(TabelaSis2, pk=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse('assunto03:assunto03_Capitulo01_Update2_View', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")  

        if action == "salvar":
            return super().post(request, *args, **kwargs)

        elif action == "deletar":
            self.object.delete()
            return HttpResponseRedirect(reverse_lazy('assunto03:assunto03_capitulo01_visualizar2_View'))

        elif action == "novo":
            return HttpResponseRedirect(reverse('assunto03:assunto03_capitulo01_cadastro_TabelaSis2_View'))       

        return super().post(request, *args, **kwargs)




#essa view é para visualizar os dados da tabela    
class assunto03_capitulo01_visualizar2_View(ListView):
    model = TabelaSis2
    template_name = 'assunto03/capitulo01/titulos/assunto03_visualizar2.html'
    paginate_by = 20
    context_object_name = 'TabelaSis2_list'
    def get_queryset(self):
        return TabelaSis2.objects.all()