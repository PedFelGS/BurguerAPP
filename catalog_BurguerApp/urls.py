from django.urls import path;
from . import views

app_name = 'catalog_BurguerApp'

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<int:id>/', views.product_detail, name='product_detail'),
    path('produtos/criar/', views.product_create, name='product_create'),
    path('produtos/<int:id>/atualizar/', views.product_update, name='product_update'),
    path('produtos/<int:id>/excluir/', views.product_delete, name='product_delete'),

    path('categorias/', views.category_list, name='category_list'),
    path('categorias/<int:id>/', views.category_detail, name='category_detail'),
    path('categorias/criar/', views.category_create, name='category_create'),
    path('categorias/<int:id>/atualizar/', views.category_update, name='category_update'),
    path('categorias/<int:id>/excluir/', views.category_delete, name='category_delete'),
]