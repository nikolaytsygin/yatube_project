"""from django.http import HttpResponse."""
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    context = {
        'text': 'Это главная страница проекта Yatube',
        'title': 'Последние обновления на сайте'
    }
    return render(request, template, context)
    # Create your views here.


def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube',
        'title': 'Лев Толстой – зеркало русской революции.'
    }
    return render(request, template, context)