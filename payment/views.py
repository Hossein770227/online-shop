import requests 
import json
from django.shortcuts import render, redirect, get_object_or_404

from orders.models import Order

def payment_process(request):
    order_id = request.session.get('order_id')

    order = get_object_or_404(Order, order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    # res = requests.post(url=)


