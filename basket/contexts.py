

def basket_contents(request):
    '''Context processor''' # makes the context dictionary available across the entire application

    basket_items = []
    total = 0
    product_count = 0

    context = {
        'basket_items' = basket_items,
        'total' = total,
        'product_count' = product_count,
    }

    return context