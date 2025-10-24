# companies/urls.py
from django.urls import path
from controles.views.companies.companiesViews import company_list_view, company_create_view, select_company_view

app_name = "companies"

urlpatterns = [
    path("company_list_view/", company_list_view, name="company_list_view"),
    path("company_create_view/", company_create_view, name="company_create_view"),
    path("select_company_view/", select_company_view, name="select_company_view"),
]