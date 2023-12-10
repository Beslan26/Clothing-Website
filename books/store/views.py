from django.shortcuts import render

from store.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'store/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'store/products.html', context)

