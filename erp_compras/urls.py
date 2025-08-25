from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Rota principal (Home)
    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')), # Rotas para solicitações
    path('pedidos/', include('pedidos.urls', namespace='pedidos')), # Rotas para pedidos
    path("cadastro/", include("cadastro.urls", namespace="cadastro")), # Rotas para cadastro
    
]
