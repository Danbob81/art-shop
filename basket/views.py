""" A view to return the shopping basket template """
from django.shortcuts import render


def basket(request):
    """ Return shopping basket page """
    return render(request, 'basket/basket.html')
