from django.urls import path;
from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/<int:id>/', views.product_detail, name='product_detail'),
    path('produtos/criar/', views.product_create, name='product_create'),
]