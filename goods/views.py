from django.shortcuts import render
from .models import Products


def catalog(req, slug):
    if slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=slug)
    context = {
        'products': products
    }
    return render(req, 'goods/catalog.html', context)


def product(req, slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(req, 'goods/product.html', context)
