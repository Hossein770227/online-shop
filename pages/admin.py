from django.contrib import admin

from .models import CallUs

@admin.register(CallUs)
class CallUsAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'date_time_created']
