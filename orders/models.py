from django.db import models

from carts.models import Cart
from goods.models import Products
from users.models import User


#
# class Delivery(models.IntegerChoices):
#     DELIVERY = 0, 'Delivery'
#     PICKUP = 1, 'Self pickup'
#
#
# class Payment(models.IntegerChoices):
#     CARD = 0, 'By card'
#     CASH = 1, 'By cash'
#
#
# class Orders(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.SET_NULL, default=None ,blank=True, null=True)
#
#     phone = models.CharField(max_length=13)
#     delivery_method = models.BooleanField(
#         choices=tuple(map(lambda x: (bool(x[0]), x[1]), Delivery.choices)),
#         default=Delivery.DELIVERY,
#         verbose_name='Delivery method'
#     )
#     delivery_address = models.CharField(max_length=300)
#     payment_method = models.BooleanField(
#         choices=tuple(map(lambda x: (bool(x[0]), x[1]), Payment.choices)),
#         default=Payment.CARD,
#         verbose_name='Payment method'
#     )
#
#     class Meta:
#         verbose_name = 'order'
#         verbose_name_plural = 'Orders'
class OrderItemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(null=True, blank=True)
    payment_on_get = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default="Pending")
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'Order #{self.pk} | Buyer: {self.user.first_name} {self.user.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "sold item"
        verbose_name_plural = "Sold items"

    object = OrderItemQueryset.as_manager()
