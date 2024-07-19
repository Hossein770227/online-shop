from django.contrib import admin

from .models import Product, Comment


class CommentTabuInline(admin.TabularInline):
    model = Comment
    list_display = ['author','active','date_time_created',]
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','active','date_time_created',]
    search_fields = ['title']
    inlines = [CommentTabuInline]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['author','product','active','date_time_created',]
#     search_fields = ['author']
