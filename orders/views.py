from django.core.exceptions import ValidationError
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages


from carts.models import Cart
from orders.forms import OrderForm
from orders.models import Order, OrderItem
from users.utils import UserLoginRequiredMixin


class CreateOrderView(UserLoginRequiredMixin, FormView):
    form_class = OrderForm
    template_name = 'orders/create_order.html'
    context_object_name = 'order'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        if self.request.user.first_name:
            self.form_class.declared_fields.get('first_name').initial = self.request.user.first_name
        if self.request.user.last_name:
            self.form_class.declared_fields.get('last_name').initial = self.request.user.last_name
        if self.request.user.phone_number:
            self.form_class.declared_fields.get('phone_number').initial = self.request.user.phone_number
        context = super().get_context_data(**kwargs)
        context['orders'] = True
        return context

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)
                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=form.cleaned_data['delivery_address'],
                        payment_on_get=form.cleaned_data['payment_on_get']
                    )
                for item in cart_items:
                    product = item.product
                    name = item.product.name
                    price = item.products_price()
                    quantity = item.quantity

                    # validation
                    if product.quantity < quantity:
                        raise ValidationError(f'Not enough product <{name}> on stock. '
                                              f'In stock - {product.quantity}')
                    if int(form.cleaned_data['requires_delivery']):
                        if not form.cleaned_data['delivery_address']:
                            raise ValidationError('Delivery address is empty')

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=name,
                        price=price,
                        quantity=quantity
                    )
                    product.quantity -= quantity
                    product.save()
                cart_items.delete()
                messages.success(self.request, 'Order was successfully done')
        except ValidationError as ex:
            messages.warning(self.request, str(*ex))
            return super().form_invalid(form)
        return super().form_valid(form)
