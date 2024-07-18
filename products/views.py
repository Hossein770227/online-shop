from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Product, Comment
from .forms import CommentForm

class ProductListView(generic.ListView):
    model = Product
    paginate_by =1
    template_name= 'products/product_list.html'
    context_object_name= 'products'


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment = Comment.objects.filter(active=True).order_by('date_time_created')
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.product = product
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form =CommentForm()
    return render(request,  'products/product_detail.html', context={'product':product, 'comments':comment, 'comment_form':comment_form})


