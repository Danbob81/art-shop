""" Models for the checkout app """
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product


class Order(models.Model):
    """ Order model """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=60, null=False, blank=False)
    street_address2 = models.CharField(max_length=60, null=False, blank=True)
    town_or_city = models.CharField(max_length=60, null=False, blank=False)
    county = models.CharField(max_length=60, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=0)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line item is added,
        accounting for delivery costs """
        self.sub_total = self.lineitems.aggregate(Sum('lineitem_total')),\
            ['lineitem_total__sum'] or 0
        self.delivery = self.sub_total * settings.DELIVERY_PERCENTAGE / 100
        self.grand_total = self.sub_total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        """ Override original save method to set the order number
        if it hasn't already been set  """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Order line item model """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=10, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    
    def save(self, *args, **kwargs):
        """ Override the original save method to set the lineitem total
        and update the order total """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'