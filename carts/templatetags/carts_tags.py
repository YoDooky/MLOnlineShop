from django import template
from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag(takes_context=True)
def user_carts(context):
    request = context['request']
    return get_user_carts(request)
