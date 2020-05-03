from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, viewsets
from ..models import Service, Subscriber, Organization, UserInfo, SubscriptionType
from .serializers import ServiceSerializer, SubscriberSerializer, OrganizationSerializer, UserInfoSerializer,SubscriptionTypeSerializer

class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubscriberView(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class OrganizationView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class UserInfoView(viewsets.ModelViewSet):
	queryset = UserInfo.objects.all()
	serializer_class = UserInfoSerializer

class SubscriptionTypeView(viewsets.ModelViewSet):
	queryset = SubscriptionType.objects.all()
	serializer_class = SubscriptionTypeSerializer