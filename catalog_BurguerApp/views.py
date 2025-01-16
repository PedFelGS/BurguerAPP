from django.shortcuts import render, get_object_or_404, redirect;
from django.http import HttpResponse
from .models import Products, Categories, User, Orders, OrderItem
from .forms import ProductForm

# Create your views here.

from django.http import HttpResponse

def product_list(req):
  if req.method == "GET":
    products = Products.objects.all()
    print(products)
    return render(req, './products/list.html', {"products": products} )
  
    '''
    # Test: serializando os produtos em um formato que possa ser convertido para JSON
    product_list = list(products.values('id', 'name', 'price', 'category__name', 'path', 'offer'))
    return JsonResponse({"products": product_list})
    ''' 

def product_create(req):
  if req.method == "POST":
    form = ProductForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect('product_list')
  else:
    form = ProductForm()
  return render(req, 'products/form.html', {'form': form})

def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/detail.html', {'product': product})
  
def product_update(request, id):
    product = get_object_or_404(Products, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/update.html', {'form': form, 'product': product})