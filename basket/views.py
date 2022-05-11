""" A view to return the shopping basket template """
from django.shortcuts import render, redirect


def view_basket(request):
    """ Return shopping basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add quantity of a product to shopping basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)