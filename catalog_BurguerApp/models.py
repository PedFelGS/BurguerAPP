from django.db import models
from django.db.models import CharField, DateTimeField, AutoField, ForeignKey, DecimalField, PositiveIntegerField, BooleanField, URLField;
from auth_BurguerApp.models import User
from django.core.exceptions import ValidationError

class Categories(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True, verbose_name='Nome da Categoria')
    path = CharField(max_length=255, verbose_name='Caminho da Imagem')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, verbose_name='Nome do Produto')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    category = ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        verbose_name='Categoria',
        null=True,
        related_name="products"
        )
    path = URLField(max_length=2000, verbose_name='Caminho da Imagem', blank=True, null=True)
    offer = BooleanField(default=False, verbose_name='Disponibilidade')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.price <= 0:
            raise ValidationError("O preço deve ser um numero positivo")

class Orders(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
    ]

    id = AutoField(primary_key=True)
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Products, through='OrderItem')
    status = CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.name}"


class OrderItem(models.Model):
    order = ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_items")
    product = ForeignKey(Products, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"
    