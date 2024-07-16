from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Comment

class ProductListView(generic.ListView):
    model = Product
    template_name= 'products/product_list.html'
    context_object_name= 'products'


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment = Comment.objects.filter(active=True)
    return render(request,  'products/product_detail.html', context={'product':product, 'comments':comment})

# class ProductDetailView(generic.DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#     context_object_name ='product'