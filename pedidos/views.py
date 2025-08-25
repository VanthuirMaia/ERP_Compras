from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pedido, ItemPedido
from cadastro.models import Fornecedor
from solicitacoes.models import Solicitacao
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings
import os, base64

def index(request):
    pedidos = Pedido.objects.all().order_by("-id").prefetch_related("itens")

    em_aberto = pedidos.filter(assinatura_comprador__isnull=True,
                               assinatura_aprovacao__isnull=True).count()
    aguardando = pedidos.filter(assinatura_comprador__isnull=False,
                                assinatura_aprovacao__isnull=True).count()
    concluidos = pedidos.filter(assinatura_comprador__isnull=False,
                                assinatura_aprovacao__isnull=False).count()

    context = {
        "page_title": "Pedidos",
        "pedidos": pedidos,
        "total_em_aberto": em_aberto + aguardando,  # se preferir separar, passe aguardando também
        "total_concluidos": concluidos,
    }
    return render(request, "pedidos/index.html", context)


def criar_pedido(request, solicitacao_id):
    solicitacao = get_object_or_404(Solicitacao, id=solicitacao_id)
    fornecedores = Fornecedor.objects.all()

    if not fornecedores.exists():
        messages.error(request, "⚠️ Cadastre ao menos um fornecedor antes de criar um pedido.")
        return redirect("fornecedores:index")

    if request.method == "POST":
        fornecedor_id = request.POST.get("fornecedor")
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

        pedido = Pedido.objects.create(
            solicitacao=solicitacao,
            fornecedor_nome=fornecedor.nome,
            fornecedor_cnpj_cpf=fornecedor.cnpj_cpf,
            fornecedor_endereco=fornecedor.endereco,
            fornecedor_cidade=fornecedor.cidade,
            fornecedor_telefone=fornecedor.telefone,
            local_entrega=request.POST.get("local_entrega"),
            prazo_entrega=request.POST.get("prazo_entrega"),
            centro_custo=request.POST.get("centro_custo"),
            condicao_pagamento=request.POST.get("condicao_pagamento"),
            observacoes=request.POST.get("observacoes"),
        )

        # Salva itens com preços informados no form
        for idx, item in enumerate(solicitacao.itens.all()):
            preco_unitario = request.POST.get(f"preco_unitario_{idx}")
            ItemPedido.objects.create(
                pedido=pedido,
                item=item.item,
                descricao=item.descricao,
                unidade="un",  # fixo ou adaptado depois
                quantidade=item.quantidade,
                preco_unitario=preco_unitario or 0,
            )

        messages.success(request, f"✅ Pedido {pedido.numero} criado com sucesso!")
        # Redireciona direto para o PDF no navegador
        return redirect("pedidos:detalhar_pedido", pk=pedido.pk)

    return render(request, "pedidos/criar_pedido.html", {
        "fornecedores": fornecedores,
        "solicitacao": solicitacao,
        "itens": solicitacao.itens.all(),
    })


def detalhar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    itens = pedido.itens.all().order_by("id")
    return render(request, "pedidos/detalhar_pedido.html", {
        "page_title": f"Pedido {pedido.numero}",
        "pedido": pedido,
        "itens": itens,
        "valor_total": pedido.valor_total,
    })

def exportar_pedido_pdf(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    itens = pedido.itens.all().order_by("id")

    # Converte logo para base64
    logo_file = os.path.join(settings.BASE_DIR, "static", "img", "miroute.png")
    logo_base64 = ""
    if os.path.exists(logo_file):
        with open(logo_file, "rb") as image_file:
            logo_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    template = get_template("pedidos/pedido_pdf.html")
    html_content = template.render({
        "pedido": pedido,
        "itens": itens,
        "valor_total": pedido.valor_total,
        "logo_base64": logo_base64,  # 🔥 agora vai sempre junto
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="pedido_{pedido.numero}.pdf"'
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse("Erro ao gerar PDF", status=500)
    return response
