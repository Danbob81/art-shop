""" A view to return the products template """
from django.shortcuts import render
from .models import Product


def products(request):
    """ Return shop page, showing products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
