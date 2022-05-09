""" A view to return the products template """
from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ Return shop page and show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Return page showing indivdual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_details.html', context)
