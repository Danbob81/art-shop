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
        'stripe_public_key':
        'pk_test_51KnSYQK8VvNqxLeBBy1xx4XSHwFOLgggsbILGg7w0pgIVbZg\
             PJB2L5JUiVBnDXP76hruUwHtOrnXHdnUW3KUhQZV0041ccBUqh',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
