from django.shortcuts import render, get_object_or_404, redirect;
from django.http import HttpResponse
from .models import Products, Categories, User, Orders, OrderItem 

# Create your views here.

from django.http import HttpResponse

def product(req):
  if req.method == "GET":
    products = Products.objects.all()
    print(products)
    return render(req, './products/list.html', {"products": products} )
  
    '''
    # Test: serializando os produtos em um formato que possa ser convertido para JSON
    product_list = list(products.values('id', 'name', 'price', 'category__name', 'path', 'offer'))
    return JsonResponse({"products": product_list})
    '''
  
  