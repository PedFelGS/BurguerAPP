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