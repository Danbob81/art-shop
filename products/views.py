""" A view to return the products template """
from django.shortcuts import render


def products(request):
    """ Return shop page """
    return render(request, 'products/products.html')
