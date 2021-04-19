from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.db.models import Q

import sweetify


def all_products(request):
    '''A view to show all of the products, including sorting and search queries'''
    
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'searchfield' in request.GET:
            query = request.GET['searchfield']
            if not query:
                sweetify.sweetalert(request, 'Search field empty', text='Please populate the search field before searching', persistent='Ok')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''A view to show detail of the chosen product'''
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)