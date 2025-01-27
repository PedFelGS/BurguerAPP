from django.test import TestCase
from django.urls import reverse, resolve
from catalog_BurguerApp import views

class CatalogVIEWsTest(TestCase): 
    def test_product_list_view_is_correct(self):
        view = resolve(reverse('catalog_BurguerApp:product_list'))
        self.assertIs(view.func, views.product_list)
        
    def test_product_detail_view_is_correct(self):
        product_id = 3
        view = resolve(reverse('catalog_BurguerApp:product_detail', kwargs={'id': product_id}))
        self.assertIs(view.func, views.product_detail)

    def test_product_create_view_is_correct(self):
        view = resolve(reverse('catalog_BurguerApp:product_create'))
        self.assertIs(view.func, views.product_create)

    def test_product_update_view_is_correct(self):
        product_id = 42
        view = resolve(reverse('catalog_BurguerApp:product_update', kwargs={'id': product_id}))
        self.assertIs(view.func, views.product_update)
    
    def test_product_delete_view_is_correct(self):
        product_id = 42
        view = resolve(reverse('catalog_BurguerApp:product_delete', kwargs={'id': product_id}))
        self.assertIs(view.func, views.product_delete)
        
        
        
        
    def test_category_list_view_is_correct(self):
        view = resolve(reverse('catalog_BurguerApp:category_list'))
        self.assertIs(view.func, views.category_list)

    def test_category_detail_view_is_correct(self):
        category_id = 12
        view = resolve(reverse('catalog_BurguerApp:category_detail', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category_detail)

    def test_category_create_view_is_correct(self):
        view = resolve(reverse('catalog_BurguerApp:category_create'))
        self.assertIs(view.func, views.category_create)

    def test_category_update_view_is_correct(self):
        category_id = 12
        view = resolve(reverse('catalog_BurguerApp:category_update', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category_update)
    
    def test_category_delete_view_is_correct(self):
        category_id = 12
        view = resolve(reverse('catalog_BurguerApp:category_delete', kwargs={'id': category_id}))
        self.assertIs(view.func, views.category_delete)
    







    def test_product_list_return_status_code_302_Found(self):
        response = self.client.get(reverse('catalog_BurguerApp:product_list'))
        self.assertEqual(response.status_code, 302)  

    def test_product_detail_return_status_code_302_Found(self):
        product_id = 3
        response = self.client.get(reverse('catalog_BurguerApp:product_detail', kwargs={'id': product_id}))
        self.assertEqual(response.status_code, 302)

    def test_product_create_return_status_code_302_Found(self):
        response = self.client.get(reverse('catalog_BurguerApp:product_create'))
        self.assertEqual(response.status_code, 302)

    def test_product_update_return_status_code_302_Found(self):
        product_id = 42
        response = self.client.get(reverse('catalog_BurguerApp:product_update', kwargs={'id': product_id}))
        self.assertEqual(response.status_code, 302) 

    def test_product_delete_return_status_code_302_Found(self):
        product_id = 42
        response = self.client.get(reverse('catalog_BurguerApp:product_delete', kwargs={'id': product_id}))
        self.assertEqual(response.status_code, 302) 




    def test_category_list_return_status_code_302_Found(self):
        response = self.client.get(reverse('catalog_BurguerApp:category_list'))
        self.assertEqual(response.status_code, 302)
    
    def test_category_detail_return_status_code_302_Found(self):
        category_id = 12
        response = self.client.get(reverse('catalog_BurguerApp:category_detail', kwargs={'id': category_id}))
        self.assertEqual(response.status_code, 302) 

    def test_category_create_return_status_code_302_Found(self):
        response = self.client.get(reverse('catalog_BurguerApp:category_create'))
        self.assertEqual(response.status_code, 302)  
    
    def test_category_update_return_status_code_302_Found(self):
        category_id = 12
        response = self.client.get(reverse('catalog_BurguerApp:category_update', kwargs={'id': category_id}))
        self.assertEqual(response.status_code, 302)  
       
    def test_category_delete_return_status_code_302_Found(self):
        category_id = 12
        response = self.client.get(reverse('catalog_BurguerApp:category_delete', kwargs={'id': category_id}))
        self.assertEqual(response.status_code, 302) 
        
