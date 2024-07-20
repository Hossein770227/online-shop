from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product

from .cart import Cart
from .forms import AddToCartForm

def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html',{'cart':cart})



def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk = product_id )
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product,quantity )
        return redirect('products:product_list')
    

def remove_form_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')