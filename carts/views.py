from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from carts.models import Cart
from goods.models import Products


def cart_add(req, product_slug):
    product = Products.objects.get(slug=product_slug)
    if req.user.is_authenticated:
        carts = Cart.objects.filter(user=req.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=req.user, product=product, quantity=1)

    return redirect(req.META['HTTP_REFERER'])


def cart_change(req, product_slug):
    pass


def cart_remove(req, cart_id):
    if req.user.is_authenticated:
        Cart.objects.get(pk=cart_id).delete()
    return redirect(req.META['HTTP_REFERER'])
