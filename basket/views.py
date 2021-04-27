from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product

import sweetify


def view_basket(request):
    '''A view to return the basket content page'''
    
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    '''Adds the item to the basket'''

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id not in basket:
        basket[item_id] = quantity
        sweetify.sweetalert(request, 'Image added to your basket', timer=1000)
    elif item_id in basket:
        sweetify.sweetalert(request, 'Image already in your basket', timer=1000)
    else:
        sweetify.sweetalert(request, 'Please try again later', text='Image could not be added at this time', persistent='Ok')

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)

        basket = request.session.get('basket', {})
        basket.pop(item_id)
        sweetify.sweetalert(request, text=f'Image {product.name} removed from basket', timer=1000)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        sweetify.sweetalert(request, text=f'Something went wrong removing {e}', persistent='Ok')
        return HttpResponse(status=500)
