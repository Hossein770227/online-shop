from django.contrib import admin

from .models import Order, OrderItem


class OrderItemTabuInline(admin.TabularInline):
    model = OrderItem
    list_display = ['product','quantity','price',]
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','email','is_paid', 'date_time_created',]
    search_fields = ['full_name']
    inlines = [OrderItemTabuInline]


# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['order','product','quantity','price',]
#     search_fields = ['order']
