from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.index, name="index"),
    # placeholders para não quebrar os links:
    path("novo/", views.criar_pedido_placeholder, name="criar_pedido"),
    path("<int:pk>/", views.detalhar_pedido_placeholder, name="detalhar_pedido"),
]
