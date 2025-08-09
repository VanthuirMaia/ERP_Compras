from django.shortcuts import render
from .models import Pedido

def index(request):
    pedidos = Pedido.objects.all().order_by('-id')
    context = {
        'page_title': 'Pedidos',
        'pedidos': pedidos
    }
    return render(request, 'pedidos/index.html', context)
