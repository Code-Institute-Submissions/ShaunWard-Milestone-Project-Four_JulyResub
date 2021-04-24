from django.shortcuts import render, redirect, reverse
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import sweetify
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        sweetify.sweetalert(request, 'Please try again later', text='There is nothing in the basket', persistent='Ok')
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        sweetify.sweetalert(request, 'Stripe Public Key Missing', text='Did you forget to set it in your environment?', persistent='Ok')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)