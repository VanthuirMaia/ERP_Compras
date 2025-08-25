from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Fornecedor

def index(request):
    fornecedores = Fornecedor.objects.all().order_by("-id")
    return render(request, "cadastro/index.html", {
        "page_title": "Fornecedores",
        "fornecedores": fornecedores
    })

def detalhar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, "cadastro/detalhar_fornecedor.html", {
        "page_title": f"Fornecedor #{fornecedor.nome}",
        "fornecedor": fornecedor
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
                "page_title": "Novo Fornecedor", "errors": errors, "data": data
            })
        Fornecedor.objects.create(**data)
        messages.success(request, "Fornecedor cadastrado com sucesso.")
        return redirect("cadastro:index")

    return render(request, "cadastro/criar_fornecedor.html", {"page_title": "Novo Fornecedor"})

def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

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
            # Re-render com erros e valores preenchidos
            return render(request, "cadastro/editar_fornecedor.html", {
                "page_title": f"Editar Fornecedor #{fornecedor.nome}",
                "errors": errors, "data": data, "fornecedor": fornecedor
            })

        # Atualiza e salva
        for field, value in data.items():
            setattr(fornecedor, field, value)
        fornecedor.save()
        messages.success(request, "Fornecedor atualizado com sucesso.")
        return redirect("cadastro:index")

    # GET: popular formulário com dados atuais
    data = {
        "nome": fornecedor.nome,
        "cnpj_cpf": fornecedor.cnpj_cpf or "",
        "endereco": fornecedor.endereco or "",
        "cidade": fornecedor.cidade or "",
        "telefone": fornecedor.telefone or "",
        "email": fornecedor.email or "",
    }
    return render(request, "cadastro/editar_fornecedor.html", {
        "page_title": f"Editar Fornecedor #{fornecedor.nome}",
        "data": data, "fornecedor": fornecedor
    })

# Excluir FORNECEDOR
def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('cadastro:index')
    return render(request, 'cadastro/excluir_fornecedor.html', {'fornecedor': fornecedor})