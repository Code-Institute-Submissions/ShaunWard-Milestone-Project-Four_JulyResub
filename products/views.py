from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm

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


def add_product(request):
    """ Add a product to the store """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('home'))

    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         product = form.save()
    #         messages.success(request, 'Successfully added product!')
    #         return redirect(reverse('product_detail', args=[product.id]))
    #     else:
    #         messages.error(request,
    #                        ('Failed to add product. '
    #                         'Please ensure the form is valid.'))
    # else:
    form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)