from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active','date_time_created',]
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','product','active','date_time_created',]
    search_fields = ['author']
