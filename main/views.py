from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(req):
    categories = Categories.objects.all()
    context = {
        'title': 'YOPT - Главная',
        'content': 'Build YOUR PC',
        'categories': categories
    }
    return render(req, 'main/index.html', context)


def about(req):
    context = {
        'title': 'YOPT - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему этот магазин такой классный, и какой хороший товар 🤢'
    }
    return render(req, 'main/about.html', context)
