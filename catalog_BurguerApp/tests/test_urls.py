from django.test import TestCase
from django.urls import reverse

class CatalogURLsTest(TestCase):

    def test_product_list_url_is_correct(self):
      list_url = reverse('catalog_BurguerApp:product_list')
      self.assertEqual(list_url, '/system/produtos/')

    def test_product_detail_url_is_correct(self):
        product_id = 3
        detail_url = reverse('catalog_BurguerApp:product_detail', kwargs={'id': product_id})
        self.assertEqual(detail_url, f'/system/produtos/{product_id}/')

    def test_product_create_url_is_correct(self):
        create_url = reverse('catalog_BurguerApp:product_create')
        self.assertEqual(create_url, '/system/produtos/criar/')
        
    def test_product_update_url_is_correct(self):
        product_id = 42
        update_url = reverse('catalog_BurguerApp:product_update', kwargs={'id': product_id})
        self.assertEqual(update_url, f'/system/produtos/{product_id}/atualizar/')




    def test_category_list_url_is_correct(self):
        list_url = reverse('catalog_BurguerApp:category_list')
        self.assertEqual(list_url, '/system/categorias/')

    def test_category_detail_url_is_correct(self):
         category_id = 12
         detail_url = reverse('catalog_BurguerApp:category_detail', kwargs={'id': category_id})
         self.assertEqual(detail_url, f'/system/categorias/{category_id}/')

    def test_category_create_url_is_correct(self):
        create_url = reverse('catalog_BurguerApp:category_create')
        self.assertEqual(create_url, '/system/categorias/criar/')

    def test_category_update_url_is_correct(self):
        category_id = 12
        update_url = reverse('catalog_BurguerApp:category_update', kwargs={'id': category_id})
        self.assertEqual(update_url, f'/system/categorias/{category_id}/atualizar/')

    def test_category_delete_url_is_correct(self):
        category_id = 12
        delete_url = reverse('catalog_BurguerApp:category_delete', kwargs={'id': category_id})
        self.assertEqual(delete_url, f'/system/categorias/{category_id}/excluir/')
    
    def test_home_url_redirects_to_login(self):
        home_url = reverse('home')
        self.assertEqual(home_url, '/')