""" Webhook handler """
from django.http import HttpResponse


class StripeWHHandler:
    """ To handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        To handle a generic/unknown/
        unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        To handle the payment_intent.succeeded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        To handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
