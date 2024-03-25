from django import template
from carts.models import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def user_carts(context):
    request = context['request']
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)



