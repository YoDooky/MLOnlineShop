from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(req):
    context = {
        'title': 'YOPT - Main page',
        'content': '',  # Build YOUR PC
    }
    return render(req, 'main/index.html', context)


def about(req):
    context = {
        'title': 'YOPT - About us',
        'content': 'About us',
        'text_on_page': 'Bla bla bla bla bla bla bla 🤢'
    }
    return render(req, 'main/about.html', context)
