""" A view to return the shop template """
from django.shortcuts import render


def shop(request):
    """ Return shop page """
    return render(request, 'shop/shop.html')
