from django.contrib import admin
from .models import Service, Subscriber, Organization, UserInfo, SubscriptionType

admin.site.register(Service)
admin.site.register(Subscriber)
admin.site.register(Organization)
admin.site.register(UserInfo)
admin.site.register(SubscriptionType)
