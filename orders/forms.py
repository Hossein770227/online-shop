from django import forms
from django.utils.translation import gettext as _

from .models import Order 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name','email','address','order_notes',]
        widgets = {
            'address':forms.Textarea(attrs={'rows':4, 'placeholder':_('please enter your address here')}),
            'order_notes':forms.Textarea(attrs={'rows':3,'placeholder':_('please enter your notes here otherwise Leave blank')}),
            }