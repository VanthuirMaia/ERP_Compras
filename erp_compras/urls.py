from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Rota principal (Home)
    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')), # Rotas para solicitações
    
]
