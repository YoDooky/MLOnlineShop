from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
