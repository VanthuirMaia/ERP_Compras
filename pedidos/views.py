from django.shortcuts import render, redirect
from .models import Pedido

def index(request):
    pedidos = Pedido.objects.all().order_by("-id").prefetch_related("itens")
    context = {
        "page_title": "Pedidos",
        "pedidos": pedidos,
        "total_em_aberto": pedidos.filter(assinatura_comprador__isnull=True).count(),
        "total_concluidos": pedidos.filter(
            assinatura_comprador__isnull=False,
            assinatura_aprovacao__isnull=False
        ).count(),
    }
    return render(request, "pedidos/index.html", context)

# PLACEHOLDERS para não dar 404 ao clicar:
def criar_pedido(request):
    if request.method == "POST":
        fornecedor_id = request.POST.get("fornecedor_id")
        fornecedor = None
        if fornecedor_id:
            fornecedor = fornecedor.objects.filter(pk=fornecedor_id).first()

        data = {
            "numero": request.POST.get("numero", "").strip(),
            "fornecedor_nome": fornecedor.nome if fornecedor else request.POST.get("fornecedor_nome", "").strip(),
            "fornecedor_cnpj_cpf": fornecedor.cnpj_cpf if fornecedor else request.POST.get("fornecedor_cnpj_cpf", "").strip(),
            "fornecedor_endereco": fornecedor.endereco if fornecedor else request.POST.get("fornecedor_endereco", "").strip(),
            "fornecedor_cidade": fornecedor.cidade if fornecedor else request.POST.get("fornecedor_cidade", "").strip(),
            "fornecedor_telefone": fornecedor.telefone if fornecedor else request.POST.get("fornecedor_telefone", "").strip(),
            "local_entrega": request.POST.get("local_entrega", "").strip(),
            "prazo_entrega": request.POST.get("prazo_entrega", "").strip(),
            "centro_custo": request.POST.get("centro_custo", "").strip(),
            "condicao_pagamento": request.POST.get("condicao_pagamento", "").strip(),
            "observacoes": request.POST.get("observacoes", "").strip(),
        }

        errors = []
        if not data["numero"]:
            errors.append("O campo 'Número' é obrigatório.")
        if not data["fornecedor_nome"]:
            errors.append("Selecione um fornecedor ou informe o nome.")
        if not data["local_entrega"]:
            errors.append("O campo 'Local de Entrega' é obrigatório.")
        if not data["centro_custo"]:
            errors.append("O campo 'Centro de Custo' é obrigatório.")
        if not data["condicao_pagamento"]:
            errors.append("O campo 'Condição de Pagamento' é obrigatório.")

        if data["numero"] and Pedido.objects.filter(numero=data["numero"]).exists():
            errors.append("Já existe um pedido com esse Número.")

        if errors:
            fornecedores = fornecedor.objects.all()
            return render(request, "pedidos/criar_pedido.html", {
                "page_title": "Novo Pedido",
                "data": data,
                "errors": errors,
                "fornecedores": fornecedores
            })

        pedido = Pedido.objects.create(**data)
        return redirect("pedidos:detalhar_pedido", pk=pedido.pk)

    fornecedores = fornecedor.objects.all()
    return render(request, "pedidos/criar_pedido.html", {
        "page_title": "Novo Pedido",
        "fornecedores": fornecedores
    })

def detalhar_pedido_placeholder(request, pk):
    return render(request, "pedidos/detalhar_pedido.html", {"page_title": f"Pedido #{pk}"})
