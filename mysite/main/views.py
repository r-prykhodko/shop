from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Home - main page',
        'content': 'Магазин мебелі',
        

    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - about us',
        'content': 'Про нас',
        'text_on_page': 'Текст про те, який наш магазин класний!'

    }

    return render(request, 'main/about.html', context)
