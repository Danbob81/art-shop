""" To calculate item subtotal in basket when quantity updated """
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculate price x quantity """
    return price * quantity
