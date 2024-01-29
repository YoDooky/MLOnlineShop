from django.shortcuts import render
from .models import Products


def catalog(req):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(req, 'goods/catalog.html', context)


def product(req):
    return render(req, 'goods/product.html')
