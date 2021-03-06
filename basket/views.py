""" A view to return the shopping basket template """
from django.shortcuts import render, redirect, reverse, HttpResponse,\
                             get_object_or_404
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ Return shopping basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add quantity of a product to shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    already_in_basket = False

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size} {product.name} quantity to\
                                     {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'{product.name} added to the\
                                         basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'{product.name} added to the basket')
    else:
        if item_id in list(basket.keys()):
            already_in_basket = True
            stock_qty = product.stock_qty
            quantity_total = int(stock_qty) + int(quantity)

            if quantity_total > stock_qty:
                messages.error(request, f"Oops! It looks like you're trying\
                                         to add more of item: '{product.name}'\
                                         than we have available.")
                return redirect(reverse('product_details', args=[product.id]))
            else:
                if not already_in_basket:
                    basket[item_id] += quantity
                    messages.success(request, f'Updated {product.name} quantity to\
                                     {basket[item_id]["items_by_size"][size]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'{product.name} added to the basket')

    print(basket)

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update quantity of a product in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size} {product.name} quantity to\
                                     {basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'{product.name} size: {size} removed from\
                             the basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to\
                             {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'{product.name} removed from\
                             the basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove a product from the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'{product.name} size: {size} removed from\
                             the basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'{product.name} removed from\
                             the basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
