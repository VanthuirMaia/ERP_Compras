from django.urls import path
from . import views

app_name = "cadastro"

urlpatterns = [
    path("fornecedores/", views.index, name="index"),
    path("fornecedores/novo/", views.criar_fornecedor, name="criar_fornecedor"),
]
