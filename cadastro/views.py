from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Fornecedor

def index(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, "cadastro/index.html", {
        "page_title": "Fornecedores",
        "fornecedores": fornecedores
    })

def criar_fornecedor(request):
    if request.method == "POST":
        data = {
            "nome": request.POST.get("nome", "").strip(),
            "cnpj_cpf": request.POST.get("cnpj_cpf", "").strip() or None,
            "endereco": request.POST.get("endereco", "").strip() or None,
            "cidade": request.POST.get("cidade", "").strip() or None,
            "telefone": request.POST.get("telefone", "").strip() or None,
            "email": request.POST.get("email", "").strip() or None,
        }
        errors = []
        if not data["nome"]:
            errors.append("O campo 'Nome' é obrigatório.")
        if errors:
            return render(request, "cadastro/criar_fornecedor.html", {
                "page_title": "Novo Fornecedor",
                "errors": errors,
                "data": data
            })
        Fornecedor.objects.create(**data)
        messages.success(request, "Fornecedor cadastrado com sucesso.")
        return redirect("cadastro:index")

    return render(request, "cadastro/criar_fornecedor.html", {"page_title": "Novo Fornecedor"})
