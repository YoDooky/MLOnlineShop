from django.contrib.sitemaps import Sitemap
from .models import Products


class ProductsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Products.objects.all()
