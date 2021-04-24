from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

import sweetify


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        sweetify.sweetalert(request, 'Please try again later', text='There is nothing in the basket', persistent='Ok')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ia0BWBpAyiaG0lOVJqLxtw1VVWuhj8tRi0TBDnxLCSkaWlPZF60uyV2zi3mNZvQUMrqAlPGPyx8gD4i9sbXInd000Z7lyp8Hg',
    }

    return render(request, template, context)