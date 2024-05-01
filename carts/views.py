from django.http import JsonResponse
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


def cart_add(req):
    product_id = req.POST.get('product_id')
    product = Products.objects.get(pk=product_id)
    if req.user.is_authenticated:
        carts = Cart.objects.filter(user=req.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=req.user, product=product, quantity=1)
    else:
        carts = Cart.objects.filter(session_key=req.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:

            Cart.objects.create(session_key=req.session.session_key, product=product, quantity=1)
    # create json response to ajax
    user_carts = get_user_carts(req)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': user_carts}, request=req
    )
    response_data = {
        'message': "Item added to cart",
        'cart_items_html': cart_items_html
    }
    return JsonResponse(response_data)


def cart_change(req):
    if req.user.is_authenticated:
        cart_id = req.POST.get('cart_id')
        quantity = req.POST.get('quantity')
        Cart.objects.filter(id=cart_id).update(quantity=quantity)
    # create json response to ajax
    user_carts = get_user_carts(req)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': user_carts}, request=req
    )
    response_data = {
        'message': "Cart items amount was changed",
        'cart_items_html': cart_items_html
    }
    return JsonResponse(response_data)


def cart_remove(req):
    quantity_deleted = 1
    if req.user.is_authenticated:
        cart_id = req.POST.get('cart_id')
        quantity_deleted = Cart.objects.get(pk=cart_id).quantity
        Cart.objects.get(pk=cart_id).delete()
    # create json response to ajax
    user_carts = get_user_carts(req)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': user_carts}, request=req
    )
    response_data = {
        'message': f"{quantity_deleted} Item(s) deleted from cart",
        'quantity_deleted': quantity_deleted,
        'cart_items_html': cart_items_html
    }
    return JsonResponse(response_data)
