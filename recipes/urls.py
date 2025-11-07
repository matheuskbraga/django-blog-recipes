from django.urls import path
from . import views

urlpatterns = [
        path('', views.receitas, name='minhas_receitas'),
        path('detalhes_receita/<int:id_receita_>/', views.detalhes_receita, name='detalhes_receita'),
        path('criar_receita/', views.criar_receita, name='criar_receita'),
        path('editar_receita/<int:id_receita_>/', views.editar_receita, name='editar_receita'),
]

