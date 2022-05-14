""" A view to return the checkout template """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ Return checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty. Continue shopping to\
                                find something you like!")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
