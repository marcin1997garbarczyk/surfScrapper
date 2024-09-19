from django.contrib import admin
from .models import Subscriber, Beach

# Register your models here.
# admin.site.register(Subscriber)

@admin.register(Beach)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'textForHtml','indexOfDay', 'totalScore']
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['pk', 'userEmail', 'trackedBeaches', 'isActive']
