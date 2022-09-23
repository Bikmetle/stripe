import json
from django.http import HttpResponse, JsonResponse
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


def CreateCheckoutSession(request, pk):
    item = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/canceled/",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": item.price,
                    "product_data": {
                        "name": item.name,
                    },
                },
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    if request.method == 'GET':
        return JsonResponse({'id': session.id})
    return redirect(session.url, code=303)
