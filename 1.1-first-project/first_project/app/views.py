from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime
from os import listdir


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime('%A, %B %d, %Y, %H:%M:%S')

    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = listdir('.')
    template_name = 'app/workdir.html'
    context = {'files': files}
    return render(request, template_name, context)
    raise NotImplemented

def hello(request):
    name = request.GET.get('name')
    return HttpResponse(f'Hello,  {name}')

def summa(request,a,b):
    result = a + b
    return HttpResponse(f'Summa ={result} ')


def demo(request):
    context = {
        'test': 'Test Hello!?',
        'data': [1,5,8,12],
    }
    return render(request,'demo1.html',context)

CONTENT = [str(i) for i in range(10000)]

def pagi(request):
    page_number = int(request.GET.get('page',1))
    paginator = Paginator(CONTENT,10)
    page =  paginator.get_page(page_number)
    context = {'page': page}
    return render(request,'pagi.html',context)

