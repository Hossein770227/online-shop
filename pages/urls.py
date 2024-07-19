from django.urls import path

from . import views

app_name ='pages'

urlpatterns = [
    path('', views.CallWithUs.as_view(), name='call_us'),
]

