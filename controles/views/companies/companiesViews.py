# companies/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Company
from controles.forms.companies.forms import CompanyForm
from django.contrib import messages

@login_required
def company_list_view(request):
    companies = Company.objects.all()
    return render(request, "templates2/companies/list.html", {"companies": companies})

@login_required
def company_create_view(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()
            messages.success(request, f"Empresa '{company.name}' criada.")
            return redirect("companies:company_list_view")
    else:
        form = CompanyForm()
    return render(request, "templates2/companies/create.html", {"form": form})

@login_required
def select_company_view(request):
    if request.method == "POST":
        company_id = request.POST.get("company_id")
        if company_id:
            try:
                company = Company.objects.get(pk=company_id)
                request.session["company_id"] = company.id
                messages.success(request, f"Empresa selecionada: {company.name}")
                next_url = request.GET.get("next") or "products:product_create_view"
                return redirect(next_url)
            except Company.DoesNotExist:
                messages.error(request, "Empresa inválida.")
        else:
            request.session.pop("company_id", None)
            messages.success(request, "Empresa desmarcada.")
    companies = Company.objects.all()
    return render(request, "templates2/companies/select.html", {"companies": companies, "current": request.session.get("company_id")})