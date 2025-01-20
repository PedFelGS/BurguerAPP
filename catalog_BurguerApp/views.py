from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Products, Categories
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.is_staff  

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')  
def product_list(req):
    if req.method == "GET":
        products = Products.objects.all()
        if req.GET.get('format') == 'json':
            product_list = list(products.values('id', 'name', 'price', 'category__name', 'path', 'offer'))
            return JsonResponse({"products": product_list})
        return render(req, 'products/list.html', {"products": products})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def product_create(req):
    if req.method == "POST":
        form = ProductForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_BurguerApp:product_list')
    else:
        form = ProductForm()
    return render(req, 'products/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def product_detail(request, id):
    product = get_object_or_404(Products, id=id)
    return render(request, 'products/detail.html', {'product': product})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def product_update(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog_BurguerApp:product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/update.html', {'form': form, 'product': product})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def product_delete(request, id):
    product = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Produto deletado com sucesso!')
        return redirect('catalog_BurguerApp:product_list')
    return render(request, 'products/delete.html', {'product': product})



@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_list(request):
    categories = Categories.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_detail(request, id):
    category = get_object_or_404(Categories, id=id)
    return render(request, 'categories/detail.html', {'category': category})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_BurguerApp:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_update(request, id):
    category = get_object_or_404(Categories, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('catalog_BurguerApp:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/update.html', {'form': form, 'category': category})

@login_required(login_url='/auth/login')
@user_passes_test(is_manager, login_url='/')
def category_delete(request, id):
    category = get_object_or_404(Categories, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('catalog_BurguerApp:category_list')
    return render(request, 'categories/delete.html', {'category': category})
