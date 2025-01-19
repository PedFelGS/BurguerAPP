from django.contrib import admin
from .models import Categories, Products, Orders, OrderItem

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('figure','name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('figure','name', 'price', 'category', 'offer', 'created_at', 'updated_at')
    list_editable = ('price', 'offer')
    search_fields = ('name',)
    list_filter = ('category', 'offer')
    ordering = ('name',)
