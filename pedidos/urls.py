from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.index, name="index"),
    path("novo/", views.criar_pedido, name="criar_pedido"),
    path("<int:pk>/", views.detalhar_pedido_placeholder, name="detalhar_pedido"),
]
