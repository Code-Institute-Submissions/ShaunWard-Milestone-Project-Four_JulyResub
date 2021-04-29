# Code Adapted from boutique ado mini project

from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    '''Context processor''' # makes the context dictionary available across the entire application

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'product': product,
        })

    delivery = 5

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
