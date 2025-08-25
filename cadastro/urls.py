from django.urls import path
from . import views

app_name = "cadastro"

urlpatterns = [
    path("fornecedores/", views.index, name="index"),
    path("fornecedores/novo/", views.criar_fornecedor, name="criar_fornecedor"),
    path("fornecedores/<int:pk>/", views.detalhar_fornecedor, name="detalhar_fornecedor"),
    path("fornecedores/<int:pk>/editar/", views.editar_fornecedor, name="editar_fornecedor"),
    path("fornecedores/<int:pk>/excluir/", views.excluir_fornecedor, name="excluir_fornecedor"),
]
