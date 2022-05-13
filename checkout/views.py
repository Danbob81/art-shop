""" A view to return the checkout template """
from django.shortcuts import render


def checkout(request):
    """ Return checkout page """
    return render(request, 'checkout/checkout.html')
