from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html', context)


def products(request):
    return render(request, 'mainapp/products.html', context)


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
