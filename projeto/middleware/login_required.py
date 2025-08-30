# projeto/settings/middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, resolve, NoReverseMatch

class LoginRequiredMiddleware:
    """
    Middleware que exige login para todas as páginas,
    exceto as listadas em PUBLIC_URL_NAMES ou prefixos liberados.
    """

    # Nomes das URLs públicas (com ou sem namespace)
    PUBLIC_URL_NAMES = {
        "principal:principal_inicio_index_view",
        "auth:login",
        "login",  # se não usar namespace
    }

    # Prefixos de caminhos sempre liberados
    PUBLIC_PATH_PREFIXES = (
        "/static/",
        getattr(settings, "MEDIA_URL", "/media/"),
        "/admin/login/",
        "/admin/js/",
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path_info

        # 1) Libera prefixos de arquivos estáticos e admin
        for prefix in self.PUBLIC_PATH_PREFIXES:
            if path.startswith(prefix):
                return self.get_response(request)

        # 2) Libera URLs públicas resolvendo o reverse
        for name in self.PUBLIC_URL_NAMES:
            try:
                url = reverse(name)
                if path == url:
                    return self.get_response(request)
            except NoReverseMatch:
                continue

        # 3) Redireciona se usuário não estiver autenticado
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
