from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView

from .models import Products


class CatalogView(ListView):
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        if self.kwargs['slug'] == 'all':
            return Products.objects.all()
        else:
            return get_list_or_404(Products.objects.filter(category__slug=self.kwargs['slug']))


# def catalog(req, slug):
#     if slug == 'all':
#         products = Products.objects.all()
#     else:
#         products = get_list_or_404(Products.objects.filter(category__slug=slug))
#
#     paginator = Paginator(products, per_page=6)
#     current_page = paginator.page(1)
#
#     context = {
#         'products': current_page
#     }
#     return render(req, 'goods/catalog.html', context)


def product(req, slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(req, 'goods/product.html', context)
