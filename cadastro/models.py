from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
