from django.shortcuts import render, redirect

from cart.cart import Cart
from orders.models import OrderItem

from .forms import OrderForm

def order_create_view(request):
    order_form = OrderForm()
    cart =Cart(request)
    if len(cart) ==0:
        return redirect('products:product_list')
    if request.method=='POST':
        order_form =OrderForm(request.POST)
        if order_form.is_valid():
            order_obj=order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order = order_obj, 
                    product = product,
                    quantity =item['quantity'],
                    price = product.price,
                )
        cart.clear()
        request.user.full_name = order_obj.full_name    
        request.user.save()
        
        request.session['order_id'] = order_obj.id

        return redirect('payment:payment_process')
    return render(request, 'orders/order_create.html', context={'form':order_form})
