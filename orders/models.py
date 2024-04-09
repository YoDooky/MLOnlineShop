from django.db import models

from carts.models import Cart
from goods.models import Products
from users.models import User


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

    def order_price(self):
        return self.orderitem_set.all().total_price()


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

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.product.display_price_with_discount() * self.quantity, 2)
