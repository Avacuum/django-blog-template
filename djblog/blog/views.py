from django.shortcuts import render
from django.http import HttpResponse

menu = ['О сайте', 'Добавить статью', 'Обратная связь']


def index(request):
    return render(request, 'blog/index.html', {'title':'main page'})


def about(request):
    return render(request, 'blog/about.html')
