from django.urls import path;
from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<int:id>/', views.product_detail, name='product_detail'),
    path('produtos/criar/', views.product_create, name='product_create'),
    path('produtos/<int:id>/atualizar/', views.product_update, name='product_update'),
    path('produtos/<int:id>/excluir/', views.product_delete, name='product_delete'),
]