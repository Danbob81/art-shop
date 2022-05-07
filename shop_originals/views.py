""" A view to return the shop_originals template """
from django.shortcuts import render


def shop_originals(request):
    """ Return shop page """
    return render(request, 'shop_originals/originals.html')
