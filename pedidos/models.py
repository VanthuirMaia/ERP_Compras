from django.db import models
from django.utils import timezone
from solicitacoes.models import Solicitacao  # importa o app de solicitações

class Pedido(models.Model):
    numero = models.CharField(max_length=20, unique=True, editable=False)
    data_emissao = models.DateField(auto_now_add=True)

    solicitacao = models.ForeignKey(
        "solicitacoes.Solicitacao",
        on_delete=models.PROTECT,
        related_name="pedidos"
    )
    numero = models.CharField(max_length=20, unique=True, editable=False)
    data_emissao = models.DateField(auto_now_add=True)
    fornecedor_nome = models.CharField(max_length=255, default='Fornecedor Não Informado')
    fornecedor_cnpj_cpf = models.CharField(max_length=20, default='00000000000000')
    fornecedor_endereco = models.CharField(max_length=255, default='Endereço Não Informado')
    fornecedor_cidade = models.CharField(max_length=100, default='Cidade Desconhecida')
    fornecedor_telefone = models.CharField(max_length=20, default='0000-0000')

    local_entrega = models.CharField(max_length=255, default='Não Informado')
    prazo_entrega = models.CharField(max_length=100, default='Não Informado')
    centro_custo = models.CharField(max_length=255, default='Centro de Custo Não Informado')
    condicao_pagamento = models.CharField(max_length=100, default='À vista')
    observacoes = models.TextField(blank=True, null=True)

    assinatura_aprovacao = models.DateTimeField(null=True, blank=True)
    assinatura_comprador = models.DateTimeField(null=True, blank=True)

    @property
    def valor_total(self):
        return sum(item.preco_total for item in self.itens.all())

    def save(self, *args, **kwargs):
        if not self.numero:
            from django.utils import timezone
            ano = timezone.now().year
            ultimo_pedido = Pedido.objects.filter(data_emissao__year=ano).order_by("id").last()
            if ultimo_pedido:
                ultimo_num = int(ultimo_pedido.numero.split("/")[0]) + 1
            else:
                ultimo_num = 1
            self.numero = f"{ultimo_num:04d}/{ano}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.numero} - {self.fornecedor_nome}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    item = models.CharField(max_length=100, default='Item Não Informado')
    descricao = models.CharField(max_length=255, default='Descrição Não Informada')
    unidade = models.CharField(max_length=20, default='un')
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    @property
    def preco_total(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.item} - {self.descricao} ({self.quantidade} x {self.preco_unitario})"
