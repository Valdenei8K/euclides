from django.urls import path
from .views import CriarProcessamentoView, StatusProcessamentoView, ListaProcessamentosView

urlpatterns = [
    path('processar/', CriarProcessamentoView.as_view(), name='processar'),
    path('status/<int:pk>/', StatusProcessamentoView.as_view(), name='status'),
    path('listar/', ListaProcessamentosView.as_view(), name='listar'),
]

