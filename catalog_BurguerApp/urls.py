from django.urls import path;
from . import views

urlpatterns = [
    path('produtos/', views.product_list, name='product_list'),
    path('produtos/create', views.product_create, name='product_create')
]