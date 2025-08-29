from django.shortcuts import render
from solicitacoes.models import Solicitacao
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("login")  # ou "core:home" se ainda não tiver login

def home(request):
    solicitacoes_recentes = Solicitacao.objects.all().order_by('-id')[:5]

    # Se não tem status, provavelmente total_pendentes e total_aprovados você calcula de outro jeito,
    # ou pode deixar estático se preferir.
    total_pendentes = 0
    total_aprovados = 0

    context = {
        'solicitacoes_recentes': solicitacoes_recentes,
        'total_pendentes': total_pendentes,
        'total_aprovados': total_aprovados,
    }
    return render(request, 'core/home.html', context)

