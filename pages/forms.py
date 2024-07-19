from django import forms

from .models import CallUs


class CallUsForm(forms.ModelForm):
    class Meta:
        model =CallUs
        fields = ['email','message',]