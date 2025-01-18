from django.shortcuts import render
from catalog_BurguerApp.models import Products, Categories

def home(request):
    category_id = request.GET.get('category')
    categories = Categories.objects.all()
    if category_id:
        products = Products.objects.filter(category_id=category_id, offer=True)
    else:
        products = Products.objects.filter(offer=True)
    return render(request, 'pages/home.html', {"products": products, 'categories': categories})

