from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.db import models
from datetime import datetime
from .models import Solicitacao, ItemSolicitacao


def index(request):
    solicitacoes = Solicitacao.objects.all().order_by('-id')
    return render(request, 'solicitacoes/index.html', {
        'solicitacoes': solicitacoes,
        'page_title': 'Solicitações'
    })


# Criar SOLICITAÇÂO
def criar_solicitacao(request):
    if request.method == 'POST':
        solicitante_nome = request.POST.get('solicitante_nome')
        programar_para = request.POST.get('programar_para')

        programar_para_date = None
        if programar_para:
            programar_para_date = datetime.strptime(programar_para, '%Y-%m-%d').date()

        solicitacao = Solicitacao.objects.create(
            solicitante_nome=solicitante_nome,
            programar_para=programar_para_date,
        )

        index = 0
        while True:
            aplicacao = request.POST.get(f'aplicacao_{index}')
            descricao = request.POST.get(f'descricao_{index}')
            especificacao = request.POST.get(f'especificacao_{index}')
            quantidade = request.POST.get(f'quantidade_{index}')
            if aplicacao and descricao and quantidade:
                ItemSolicitacao.objects.create(
                    solicitacao=solicitacao,
                    item=index + 1,
                    aplicacao=aplicacao,
                    descricao=descricao,
                    especificacao=especificacao or '',
                    quantidade=int(quantidade),
                )
                index += 1
            else:
                break

        return redirect('solicitacoes:index')

    return render(request, 'solicitacoes/criar_solicitacao.html')


# Detalhar SOLICITAÇÂO
def detalhar_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    itens = solicitacao.itens.all()  # iteração dos itens relacionados
    return render(request, 'solicitacoes/detalhar_solicitacao.html', {
        'solicitacao': solicitacao,
        'itens': itens,
        'page_title': f'Solicitação #{solicitacao.id}'
    })

# Editar SOLICITAÇÂO
@require_http_methods(["GET", "POST"])
def editar_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, id=pk)
    itens = ItemSolicitacao.objects.filter(solicitacao=solicitacao).order_by('item')

    if request.method == 'POST':
        solicitacao.solicitante_nome = request.POST.get('solicitante_nome')
        solicitacao.programar_para = request.POST.get('programar_para') or None
        solicitacao.save()

        # Dados dos itens existentes
        item_ids = request.POST.getlist('item_id')
        aplicacoes = request.POST.getlist('aplicacao')
        descricoes = request.POST.getlist('descricao')
        especificacoes = request.POST.getlist('especificacao')
        quantidades = request.POST.getlist('quantidade')

        # Atualiza ou remove os itens existentes
        for i, item_id in enumerate(item_ids):
            item = get_object_or_404(ItemSolicitacao, id=item_id)

            # Verifica se o checkbox de remover está marcado
            if request.POST.get(f'remover_{i}') == 'on':
                item.delete()
                continue

            # Atualiza campos
            item.aplicacao = aplicacoes[i]
            item.descricao = descricoes[i]
            item.especificacao = especificacoes[i]
            item.quantidade = int(quantidades[i]) if quantidades[i] else 0
            item.save()

        # Refaz a queryset atualizada depois de possíveis exclusões
        itens = ItemSolicitacao.objects.filter(solicitacao=solicitacao).order_by('item')

        # Adiciona novos itens (os extras que vieram nos inputs)
        # Novos itens serão os que estão após o total de itens existentes no array
        total_existentes = len(item_ids)
        for i in range(total_existentes, len(aplicacoes)):
            if aplicacoes[i].strip() and descricoes[i].strip() and quantidades[i].strip():
                # Calcula o próximo número do item sequencialmente (considerando itens atuais)
                max_item = itens.aggregate(models.Max('item'))['item__max'] or 0
                proximo_item_num = max_item + 1

                ItemSolicitacao.objects.create(
                    solicitacao=solicitacao,
                    item=proximo_item_num,
                    aplicacao=aplicacoes[i],
                    descricao=descricoes[i],
                    especificacao=especificacoes[i],
                    quantidade=int(quantidades[i]),
                )

                # Atualiza queryset após inserção
                itens = ItemSolicitacao.objects.filter(solicitacao=solicitacao).order_by('item')

        return redirect('solicitacoes:detalhar_solicitacao', solicitacao.id)

    return render(request, 'solicitacoes/editar_solicitacao.html', {
        'solicitacao': solicitacao,
        'itens': itens,
        'page_title': f'Editar Solicitação #{solicitacao.id}'
    })


# Excluir SOLICITAÇÂO
def excluir_solicitacao(request, pk):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('solicitacoes:index')
    return render(request, 'solicitacoes/excluir_solicitacao.html', {'solicitacao': solicitacao})

# Remover Item de Solicitação
@require_POST
def remover_item(request, item_id):
    item = get_object_or_404(ItemSolicitacao, id=item_id)
    solicitacao_id = item.solicitacao.id
    item.delete()
    return redirect('solicitacoes:editar_solicitacao', pk=solicitacao_id)