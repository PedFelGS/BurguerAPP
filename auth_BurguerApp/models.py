import uuid
from django.db import models
from django.db.models.fields import CharField, EmailField, BooleanField, DateTimeField, UUIDField, AutoField;

class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = CharField(max_length=255)
    email = EmailField(unique=True)
    password_hash = CharField(max_length=255)
    admin = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

'''

Comandos SQLITE para a tabela User:

1. Inserir um usuário:
INSERT INTO auth_burguerapp_user (id, name, email, password_hash, admin, created_at, updated_at) 
VALUES (hex(randomblob(16)), 'João Silva', 'joao.silva@example.com', 'hash_senha1', FALSE, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

2. Consulta de todos os usuários:
SELECT * FROM auth_burguerapp_user

'''