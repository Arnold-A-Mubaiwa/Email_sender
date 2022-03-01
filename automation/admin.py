from django.contrib import admin
from .models import Email, Subscriber, Subscription
# Register your models here.

class SubscribersInline(admin.TabularInline):
    model = Subscriber
    extra = 0

class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubscribersInline]

admin.site.register(Email)
admin.site.register(Subscription, SubscriptionAdmin)