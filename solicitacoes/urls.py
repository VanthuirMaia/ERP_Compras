from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('', views.index, name='index'),
]
