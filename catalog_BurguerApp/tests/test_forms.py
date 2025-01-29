from django.test import TestCase
from catalog_BurguerApp.models import Products, Categories
from catalog_BurguerApp.forms import ProductForm, CategoryForm
from django.core.exceptions import ValidationError

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Categories.objects.create(
            name="Bebidas",
        )
        self.assertEqual(category.name, "Bebidas")
        self.assertFalse(bool(category.image))



class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name="Lanches")

    def test_create_product(self):
        product = Products.objects.create(
            name="X-Burguer",
            price=25.50,
            category=self.category
        )
        self.assertEqual(product.name, "X-Burguer")
        self.assertEqual(product.price, 25.50)
        self.assertEqual(product.category, self.category)

    def test_product_price_validation(self):
        with self.assertRaises(ValidationError):
            product = Products(
                name="X-Burguer",
                price=-10,
                category=self.category
            )
            product.clean()


class CategoryFormTest(TestCase):
    def test_valid_category_form(self):
        form_data = {
            "name": "Sobremesas",
        }
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_category_form(self):
        form_data = {
            "name": "",
        }
        form = CategoryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class ProductFormTest(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(name="Lanches")

    def test_valid_product_form(self):
        form_data = {
            "name": "X-Tudo",
            "price": 30.00,
            "category": self.category.id,
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())