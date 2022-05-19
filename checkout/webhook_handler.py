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
            content=f'Webhook received: {event["type"]}',
            status=200)
