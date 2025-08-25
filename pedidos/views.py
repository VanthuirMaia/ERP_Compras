from django.shortcuts import render
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
def criar_pedido_placeholder(request):
    return render(request, "pedidos/criar_pedido.html", {"page_title": "Novo Pedido"})

def detalhar_pedido_placeholder(request, pk):
    return render(request, "pedidos/detalhar_pedido.html", {"page_title": f"Pedido #{pk}"})
