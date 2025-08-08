from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('', views.index, name='index'),
    path('criar/', views.criar_solicitacao, name='criar_solicitacao'), # Criar
    path('<int:pk>/', views.detalhar_solicitacao, name='detalhar_solicitacao'), # Detalhar
    path('<int:pk>/editar/', views.editar_solicitacao, name='editar_solicitacao'), # Editar
    path('<int:pk>/excluir/', views.excluir_solicitacao, name='excluir_solicitacao'), # Excluir
    path('item/<int:item_id>/remover/', views.remover_item, name='remover_item'),

]
