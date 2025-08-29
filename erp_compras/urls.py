from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Rota principal (Home)
    path('home/', lambda request: redirect('core:home'), name='home'),

    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')), # Rotas para solicitações
    path('pedidos/', include('pedidos.urls', namespace='pedidos')), # Rotas para pedidos
    path("cadastro/", include("cadastro.urls", namespace="cadastro")), # Rotas para cadastro
    path("sem-permissao/", lambda request: render(request, "sem_permissao.html"), name="sem_permissao"),

        # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="login"), name="logout"),
]
