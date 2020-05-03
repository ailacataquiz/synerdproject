from rest_framework import serializers
from ..models import Service, Subscriber, Organization, UserInfo, SubscriptionType


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ('serviceCode', 'serviceName', 'description','premium','allocation')

class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscriber
		fields = ('subscriberID','username','subscriptionTypeCode','serviceCode',
			'requestDate','startDate','endDate','motifOfCancellation')


class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organization
		fields = ('organizationCode','organizationName','description','dateJoined',
			'address1','address2','city','zipcode','state','phoneNumber')

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserInfo
		fields = ('username', 'firstName','lastName')


class SubscriptionTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = SubscriptionType
		fields = ('subscriptionTypeCode', 'subscriptionTypeName')
