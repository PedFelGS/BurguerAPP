from django.db import models
from django.db.models import CharField, DateTimeField, AutoField, ForeignKey, DecimalField, PositiveIntegerField, BooleanField;
from auth_BurguerApp.models import User
from django.core.exceptions import ValidationError

class Categories(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255, unique=True)
    path = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

'''

Comandos SQLITE para a tabela Categories:

1. Inserir uma nova categoria:
INSERT INTO catalog_BurguerApp_categories (name, path, created_at, updated_at) 
VALUES ('Bebidas', '/images/bebidas.png', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

2. Inserir várias categorias:
INSERT INTO catalog_burguerapp_categories (name, path, created_at, updated_at) 
VALUES 
('Aperitivos', '/images/aperitivos.png', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Sobremesas', '/images/sobremesas.png', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Combos', '/images/combos.png', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

3. Consulta de todas as categorias:
SELECT * FROM catalog_BurguerApp_categories;

'''



class Products(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
        )
    path = CharField(max_length=255)
    offer = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.price <= 0:
            raise ValidationError("O preço deve ser um numero positivo")

'''

Comandos SQL para a tabela Products:

1. Inserir um produto:
INSERT INTO catalog_BurguerApp_products (name, price, category_id, path, offer, created_at, updated_at) 
VALUES ('Hambúrguer Clássico', '19.90', 1, '/images/classico.png', FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

2. Inserir vários produtos:
INSERT INTO catalog_burguerapp_products 
(name, price, category_id, path, offer, created_at, updated_at) 
VALUES 
('Batata Frita Média', '14.90', 2, '/images/batata.png', FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Refrigerante Lata', '5.90', 3, '/images/refrigerante.png', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Combo Clássico', '29.90', 5, '/images/combo_classico.png', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Milkshake Chocolate', '12.90', 4, '/images/milkshake_chocolate.png', TRUE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

3. Consulta de todos os produtos:
SELECT * FROM catalog_BurguerApp_products;

'''



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

'''

Comandos SQL para a tabela Orders:

1. Inserir um pedido:
INSERT INTO catalog_burguerapp_orders (user_id, status, created_at, updated_at) 
VALUES 
((SELECT id FROM auth_burguerapp_user WHERE name = 'João Silva'), 'CONFIRMED', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

2. Consultar todos os pedidos:
SELECT * FROM catalog_BurguerApp_orders;

'''


class OrderItem(models.Model):
    order = ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_items")
    product = ForeignKey(Products, on_delete=models.CASCADE)
    quantity = PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"
    
'''

Comandos SQL para a tabela OrderItem:

1. Inserir itens no pedido:
INSERT INTO catalog_burguerapp_orderitem (order_id, product_id, quantity) 
VALUES 
(1, (SELECT id FROM catalog_burguerapp_products WHERE name = 'Hambúrguer Clássico'), 2),
(1, (SELECT id FROM catalog_burguerapp_products WHERE name = 'Batata Frita Média'), 1);

2. Consultar todos os itens do pedido:
SELECT * FROM catalog_BurguerApp_orderitem;

'''