# ========================================
# SOLUÇÃO 7: VIEWS CORRIGIDAS
# core/views.py (CRIAR ARQUIVO)
# ========================================
#
#from django.shortcuts import render, redirect
#from django.contrib.auth.decorators import login_required
#from django.contrib import messages
#from controles.models import Empresas, UsuarioEmpresa
#
#@login_required
#def selecionar_empresa(request):
#    """View para usuário escolher qual empresa quer trabalhar."""
#    
#    # Obtém empresas disponíveis
#    vinculos = UsuarioEmpresa.objects.filter(
#        usuario=request.user,
#        ativo=True,
#        empresa__ativa=True
#    ).select_related('empresa').order_by('empresa__nome')
#    
#    if vinculos.count() == 0:
#        messages.error(request, "Você não tem empresas vinculadas.")
#        return redirect('auth:logout')
#    
#    # Processa seleção
#    if request.method == 'POST':
#        empresa_id = request.POST.get('empresa_id')
#        vinculo = vinculos.filter(empresa_id=empresa_id).first()
#        
#        if vinculo:
#            request.session['empresa_id'] = vinculo.empresa.id
#            messages.success(
#                request, 
#                f"✓ Empresa '{vinculo.empresa.nome}' selecionada!"
#            )
#            
#            # Redireciona
#            next_url = request.GET.get('next') or request.POST.get('next')
#            if next_url and next_url != '/selecionar-empresa/':
#                return redirect(next_url)
#            return redirect('home:home_inicio_View')
#        else:
#            messages.error(request, "Empresa inválida.")
#    
#    # Renderiza formulário
#    context = {
#        'vinculos': vinculos,
#        'empresa_atual_id': request.session.get('empresa_id'),
#        'next': request.GET.get('next', ''),
#    }
#    
#    return render(request, 'core/selecionar_empresa.html', context)
#
#
#@login_required
#def trocar_empresa(request, empresa_id):
#    """View rápida para trocar de empresa."""
#    
#    # Verifica se usuário tem acesso
#    vinculo = UsuarioEmpresa.objects.filter(
#        usuario=request.user,
#        empresa_id=empresa_id,
#        ativo=True,
#        empresa__ativa=True
#    ).select_related('empresa').first()
#    
#    if vinculo:
#        request.session['empresa_id'] = vinculo.empresa.id
#        messages.success(request, f"✓ Trocado para: {vinculo.empresa.nome}")
#    else:
#        messages.error(request, "✗ Acesso negado.")
#    
#    # Retorna para página anterior
#    next_url = request.GET.get('next') or request.META.get('HTTP_REFERER', '/')
#    return redirect(next_url)
#