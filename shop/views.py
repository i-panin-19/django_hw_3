from django.shortcuts import render

from shop.models import Product, Category


def index(request):
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all(),
        'title': 'Магазин "Ромашка"',
    }
    return render(request, 'shop/index.html', context)
