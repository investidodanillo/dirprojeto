# controles\views\products\productsViews.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from controles.models.products.models import Product
from controles.forms.products.forms import ProductForm
from django.contrib import messages

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "templates2/products/list.html", {"products": products, "current_company": request.current_company})

@login_required
def product_create_view(request):
    if not request.current_company:
        messages.warning(request, "Selecione uma empresa antes de cadastrar produtos.")
        return redirect("companies:select")
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.company = request.current_company
            p.save()
            messages.success(request, "Produto criado.")
            return redirect("products:product_list_view")
    else:
        form = ProductForm()
    return render(request, "templates2/products/create.html", {"form": form, "current_company": request.current_company})

@login_required
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado.")
            return redirect("products:product_list_view")
    else:
        form = ProductForm(instance=product)
    return render(request, "products/update.html", {"form": form, "product": product})