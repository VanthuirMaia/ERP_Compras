from django.db import models

class Solicitacao(models.Model):
    STATUS_CHOICES = [
        ("aberta", "Aberta"),
        ("em_analise", "Em análise"),
        ("aprovada", "Aprovada"),
        ("convertida", "Convertida em Pedido"),
        ("cancelada", "Cancelada"),
    ]

    solicitante_nome = models.CharField(max_length=100)
    data_solicitacao = models.DateField(auto_now_add=True)
    programar_para = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="aberta")

    def __str__(self):
        return f"Solicitação #{self.id} - {self.solicitante_nome}"


class ItemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='itens')
    item = models.IntegerField()
    aplicacao = models.CharField(max_length=255, blank=True)
    descricao = models.CharField(max_length=255)
    especificacao = models.TextField(blank=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Item {self.item} - {self.descricao}"
