from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.index, name="index"),
    path("novo/<int:solicitacao_id>/", views.criar_pedido, name="criar_pedido"),
    path("<int:pk>/", views.detalhar_pedido, name="detalhar_pedido"),
    path("<int:pk>/pdf/", views.exportar_pedido_pdf, name="exportar_pedido_pdf"),

]
