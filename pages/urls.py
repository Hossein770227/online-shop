from django.urls import path

from . import views

app_name ='pages'

urlpatterns = [
    path('', views.call_with_us, name='call_us'),
]

