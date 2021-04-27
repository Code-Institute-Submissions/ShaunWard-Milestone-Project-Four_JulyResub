from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, 'Sorry, only store owners can do that.', timer=1000)
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            sweetify.sweetalert(request, 'Success! Product Added', timer=1000)
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            sweetify.sweetalert(request, 'Failed to add product.', text='Please ensure the form is valid.', persistent='Ok')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, 'Sorry, only store owners can do that.', timer=1000)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            sweetify.sweetalert(request, 'Success! Product Updated', timer=1000)
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            sweetify.sweetalert(request, title='Failed to update product.', text='Please ensure the form is valid.', timer=1000)
    else:
        form = ProductForm(instance=product)
        sweetify.sweetalert(request, f'You are editing {product.name}', timer=1000)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        sweetify.sweetalert(request, 'Sorry, only store owners can do that.', timer=1000)
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    sweetify.sweetalert(request, 'Product deleted', timer=1000)
    return redirect(reverse('products'))
