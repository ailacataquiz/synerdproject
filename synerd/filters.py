import django_filters 
from django_filters import CharFilter
from .models import *

class UserInfoFilter(django_filters.FilterSet):
	firstname = CharFilter(field_name='username__firstName', lookup_expr='icontains')
	lastname = CharFilter(field_name='username__lastName', lookup_expr='icontains')


	class Meta:
		model =  Subscriber
		fields = ['subscriberID','username']