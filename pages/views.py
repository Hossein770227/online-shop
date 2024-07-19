from django.shortcuts import render
from django.views import generic

from .forms import CallUsForm
from .models import CallUs

def call_with_us(request):
    if request.method =='POST':
        form = CallUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = CallUsForm()
    else:
        form = CallUsForm()
        return render(request, 'pages/call_with_us.html', {'form':form})
    
# class CallWithUs(generic.CreateView):
#     model = CallUs
#     form_class = CallUsForm
#     template_name = 'pages/call_with_us.html'
