from django.test import TestCase
from django.urls import reverse
from auth_BurguerApp.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User


class AuthURLSTest(TestCase):
    def test_burguerapp_login_url_is_correct(self):
        login_url = reverse("auth_BurguerApp:login_view")
        self.assertEqual(login_url, "/auth/login/")

    def test_burguerapp_logout_url_is_correct(self):
        logout_url = reverse("auth_BurguerApp:logout_view")
        self.assertEqual(logout_url, "/auth/logout/")

    def test_burguerapp_register_url_is_correct(self):
        register_url = reverse("auth_BurguerApp:register_view")
        self.assertEqual(register_url, "/auth/register/")


class UserRegisterFormTest(TestCase):
    def test_formulario_de_registro_valido(self):
        # Dados válidos para registro
        form_data = {
            "name": "Usuário Teste",
            "email": "usuarioteste@example.com",
            "password": "senhaForte123",
            "confirm_password": "senhaForte123",
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formulario_de_registro_invalido_por_senhas_diferentes(self):
        # Teste quando as senhas não correspondem
        form_data = {
            "name": "Usuário Teste",
            "email": "usuarioteste@example.com",
            "password": "senha123",
            "confirm_password": "senhaDiferente123",
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("As senhas não correspondem.", form.errors["__all__"])

    def test_formulario_de_registro_invalido_por_email_ausente(self):
        # Teste quando o email não é fornecido
        form_data = {
            "name": "Usuário Teste",
            "password": "senha123",
            "confirm_password": "senha123",
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class UserLoginFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criação de um usuário para testes de login
        cls.user = User.objects.create_user(
            username="usuarioteste",
            password="senha123",
            email="usuarioteste@example.com",
        )

    def test_formulario_de_login_valido(self):
        # Teste com dados válidos para login
        form_data = {"username": "usuarioteste", "password": "senha123"}
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formulario_de_login_invalido_por_nome_de_usuario_errado(self):
        # Teste com nome de usuário incorreto
        form_data = {"username": "usuarioerrado", "password": "senha123"}
        form = UserLoginForm(data=form_data)
        self.assertTrue(
            form.is_valid()
        ) 

    def test_formulario_de_login_invalido_por_campos_ausentes(self):
        # Teste com campos ausentes
        form_data = {"username": ""}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("password", form.errors)
