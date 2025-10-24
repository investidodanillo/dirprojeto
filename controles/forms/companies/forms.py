# companies/forms.py
from django import forms
from core.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "cnpj"]