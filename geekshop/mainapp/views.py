from django.shortcuts import render
from .models import ProductCategory, Product
import random as rnd

def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}

    return render(request, 'mainapp/index.html', content)


def products(request):
    title = 'Продукция'
    products = Product.objects.all()
    products_sample = Product.objects.all()[:3]
    #rnd.shuffle(products_sample)

    content = {'title': title, 'products': products, 'products_sample': products_sample}

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def test(request):
    return render(request, 'mainapp/test.html', context)


context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт',
        'user': 'Николай',
        'products': [
            {
                'name': 'Стул 1',
                'price': 3000,
                'notice': 'Просто хороший стул',
                'img': 'img/1.jpg'
            },
            {
                'name': 'Стул 2',
                'price': 5000,
                'notice': 'Стул получше среднего',
                'img': 'img/2.jpg'
            },
            {
                'name': 'Стол 1',
                'price': 6000,
                'notice': 'Стол как стол',
                'img': 'img/3.jpg'
            }
        ]
    }
