""" Admin """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    """ Order line item admin """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Order admin """
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = (
        'order_number', 'date', 'delivery',
        'sub_total', 'grand_total',
    )

    fields = (
        'order_number', 'date', 'full_name',
        'email', 'phone_number', 'street_address1',
        'street_address2', 'town_or_city', 'county',
        'postcode', 'country', 'sub_total', 'delivery',
        'grand_total',
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'sub_total', 'delivery', 'grand_total',
    )

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
