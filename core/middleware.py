# core/middleware.py
# core/middleware.py
from django.shortcuts import get_object_or_404
from core.models import Company
from core.threadlocal import set_current_company, set_current_company_id

class CompanySessionMiddleware:
    """
    Middleware que lê request.session['company_id'] e popula threadlocal
    com a empresa corrente. Também anexa request.current_company.
    Deve vir **depois** do AuthenticationMiddleware.

    tenant_id = é o company_id
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        company = None
        company_id = request.session.get("company_id")
        if company_id:
            try:
                company = Company.objects.filter(pk=company_id).first()
            except Exception:
                company = None
        # set in threadlocal
        set_current_company(company)
        set_current_company_id(company.id if company else None)
        # attach to request
        request.current_company = company
        return self.get_response(request)
    

