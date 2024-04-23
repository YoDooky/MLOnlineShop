from django.contrib import admin
from django.contrib.auth.models import Permission

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [CartTabAdmin, OrderTabularAdmin]


@admin.register(Permission)
class UserPermissionAdmin(admin.ModelAdmin):
    pass
