# Generated by Django 4.2.7 on 2024-04-09 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'cart', 'verbose_name_plural': 'Carts'},
        ),
    ]
