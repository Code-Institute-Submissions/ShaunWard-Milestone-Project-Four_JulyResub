from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    '''Context processor''' # makes the context dictionary available across the entire application

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        basket_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context
