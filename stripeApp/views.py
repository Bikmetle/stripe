from django.shortcuts import render, redirect, get_object_or_404
import stripe
from requests import Response

from .models import Item
from django.conf import settings
stripe.api_key = settings.STRIPE_SK


def LandingPage(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'landing.html', {'item': item})


def Success(requst):
    return render(requst, 'success.html')


def Canceled(request):
    return render(request, 'canceled.html')


def CreateCheckoutSession(request):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            success_url="http://localhost:8000/success/",
            cancel_url="http://localhost:8000/canceled/",
            line_items=[
                {
                    "price": "price_1LjimQGQ7a1wQCsd9WsQeVHS",
                    "quantity": 2,
                },
            ],
            mode="payment",
        )
        return redirect(session.url, code=303)
