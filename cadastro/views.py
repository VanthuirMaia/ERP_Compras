from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Fornecedor
from django.contrib.auth.decorators import login_required, user_passes_test

# Grupos
def is_solicitante(user):
    return user.groups.filter(name="Solicitante").exists() or user.is_superuser

def is_compras(user):
    return user.groups.filter(name="Compras").exists() or user.is_superuser

def is_gerencia(user):
    return user.groups.filter(name="Gerência").exists() or user.is_superuser



# =========================
# FORNECEDORES
# =========================

def index(request):
    fornecedores = Fornecedor.objects.all().order_by("-id")
    return render(request, "cadastro/fornecedores/index.html", {
        "page_title": "Fornecedores",
        "fornecedores": fornecedores
    })


def detalhar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, "cadastro/fornecedores/detalhar.html", {
        "page_title": f"Fornecedor #{fornecedor.nome}",
        "fornecedor": fornecedor
    })

@login_required
@user_passes_test(is_compras, login_url='/sem-permissao/')
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
            return render(request, "cadastro/fornecedores/criar.html", {
                "page_title": "Novo Fornecedor", "errors": errors, "data": data
            })
        Fornecedor.objects.create(**data)
        messages.success(request, "Fornecedor cadastrado com sucesso.")
        return redirect("cadastro:index")

    return render(request, "cadastro/fornecedores/criar.html", {"page_title": "Novo Fornecedor"})

@login_required
@user_passes_test(is_compras, login_url='/sem-permissao/')
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
            return render(request, "cadastro/fornecedores/editar.html", {
                "page_title": f"Editar Fornecedor #{fornecedor.nome}",
                "errors": errors, "data": data, "fornecedor": fornecedor
            })

        for field, value in data.items():
            setattr(fornecedor, field, value)
        fornecedor.save()
        messages.success(request, "Fornecedor atualizado com sucesso.")
        return redirect("cadastro:index")

    data = {
        "nome": fornecedor.nome,
        "cnpj_cpf": fornecedor.cnpj_cpf or "",
        "endereco": fornecedor.endereco or "",
        "cidade": fornecedor.cidade or "",
        "telefone": fornecedor.telefone or "",
        "email": fornecedor.email or "",
    }
    return render(request, "cadastro/fornecedores/editar.html", {
        "page_title": f"Editar Fornecedor #{fornecedor.nome}",
        "data": data, "fornecedor": fornecedor
    })

@login_required
@user_passes_test(is_compras, login_url='/sem-permissao/')
def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('cadastro:index')
    return render(request, 'cadastro/fornecedores/excluir.html', {'fornecedor': fornecedor})


# =========================
# USUÁRIOS
# =========================

def lista_usuarios(request):
    usuarios = User.objects.all().order_by("id")
    return render(request, "cadastro/usuarios/lista.html", {
        "page_title": "Usuários",
        "usuarios": usuarios
    })


def criar_usuario(request):
    grupos = Group.objects.all()
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        grupo_id = request.POST.get("grupo")

        user = User.objects.create_user(
            username=email,  # username = email
            email=email,
            password=senha,
            first_name=nome
        )
        if grupo_id:
            grupo = Group.objects.get(id=grupo_id)
            user.groups.add(grupo)

        messages.success(request, f"Usuário {nome} criado com sucesso.")
        return redirect("cadastro:lista_usuarios")

    return render(request, "cadastro/usuarios/form.html", {
        "page_title": "Novo Usuário",
        "grupos": grupos
    })
