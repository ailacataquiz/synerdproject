from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('service', views.ServiceView)
router.register('subscriber', views.SubscriberView)
router.register('organization', views.OrganizationView)
router.register('userinfo', views.UserInfoView)
router.register('subscriptiontype', views.SubscriptionTypeView)

urlpatterns = [
    path('', include(router.urls))
]