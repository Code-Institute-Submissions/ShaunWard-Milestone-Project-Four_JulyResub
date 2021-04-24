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
    }

    return render(request, template, context)