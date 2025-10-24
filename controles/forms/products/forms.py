# products/forms.py
from django import forms
from controles.models.products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "description", "quantity"]