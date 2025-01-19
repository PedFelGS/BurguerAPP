from django.shortcuts import render, redirect
from catalog_BurguerApp.models import Products, Categories
from django.http import JsonResponse
def home(request):
    if 'carrinho' not in request.session:
        request.session['carrinho'] = []
    
    category_id = request.GET.get('category')
    categories = Categories.objects.all()
    if category_id:
        products = Products.objects.filter(category_id=category_id, offer=True)
    else:
        products = Products.objects.filter(offer=True)
    return render(request, 'pages/home.html', {
        "products": products,
        'categories': categories,
        "carrinho": len(request.session['carrinho'])
    })

def add_to_cart(request, product_id):
    if request.method == 'POST':
        if 'carrinho' not in request.session:
            request.session['carrinho'] = []
        
        carrinho = request.session['carrinho']
        carrinho.append(product_id)
        request.session['carrinho'] = carrinho
        request.session.modified = True
        
        return JsonResponse({'status': 'success', 'cart_count': len(carrinho)})
    
    return JsonResponse({'status': 'error'}, status=400)

def view_cart(request):
    if 'carrinho' not in request.session:
        request.session['carrinho'] = []
    
    cart_items = []
    total = 0
    for product_id in request.session['carrinho']:
        product = Products.objects.get(id=product_id)
        cart_items.append(product)
        total += product.price
    
    return render(request, 'pages/cart.html', {
        'cart_items': cart_items,
        'total': total,
        'carrinho': len(request.session['carrinho'])
    })

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        if 'carrinho' in request.session:
            carrinho = request.session['carrinho']
            if product_id in carrinho:
                carrinho.remove(product_id)
                request.session['carrinho'] = carrinho
                request.session.modified = True
        
        return redirect('view_cart')
    
    return JsonResponse({'status': 'error'}, status=400)