# core/middleware.py
from django.utils.deprecation import MiddlewareMixin
from .threadlocal import set_current_empresa  # Use threadlocal

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Só define a empresa se o usuário estiver autenticado
        if request.user.is_authenticated and hasattr(request.user, 'empresa'):
            set_current_empresa(request.user.empresa)
        else:
            set_current_empresa(None)

    def process_response(self, request, response):
        # Limpa o threadlocal após a requisição
        from .threadlocal import set_current_empresa
        set_current_empresa(None)
        return response
