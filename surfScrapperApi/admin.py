from django.contrib import admin
from .models import Subscriber

# Register your models here.
# admin.site.register(Subscriber)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['pk', 'userEmail', 'trackedBeaches', 'isActive']
