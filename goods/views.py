from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView
from django.http import Http404

from .models import Products
from .utils import query_search


class CatalogView(ListView):
    model = Products
    template_name = 'goods/catalog.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        on_sale = self.request.GET.get('on_sale', None)
        order_by = self.request.GET.get('order_by', None)
        query = self.request.GET.get('query', None)

        products = Products.objects.all()
        if query:
            products = query_search(query)
        if on_sale:
            products = products.filter(discount__gt=0)
        if order_by and order_by != 'default':
            products = products.order_by(order_by)
        if self.kwargs.get('slug') and self.kwargs.get('slug') != 'all':
            products = get_list_or_404(products.filter(category__slug=self.kwargs.get('slug')))
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['slug'] = self.kwargs.get('slug')
        context['on_sale_filter'] = self.request.GET.get('on_sale', None)
        context['order_by_filter'] = self.request.GET.get('order_by', None)
        context['search_filter'] = self.request.GET.get('query', None)
        return context


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
