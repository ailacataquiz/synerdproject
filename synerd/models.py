
from django.db import models

class UserInfo(models.Model):
	username = models.CharField(primary_key=True, max_length=20)

	firstName = models.CharField(max_length=20)
	middleName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)

	email = models.CharField(max_length=40)

	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=10)

	employerName = models.CharField(max_length=20)

	def __str__(self):
		return self.username
		

class Service(models.Model):
	serviceCode = models.IntegerField(primary_key=True)
	serviceName = models.CharField(max_length=20)
	description = models.TextField()
	premium = models.CharField(max_length=20)
	allocation = models.CharField(max_length=20)

	def __str__(self):
		return self.serviceName


class SubscriptionType(models.Model):
	subscriptionTypeCode = models.IntegerField(primary_key=True)
	subscriptionTypeName = models.CharField(max_length=20)

	def __str__(self):
		return self.subscriptionTypeName


class Subscriber(models.Model):
	subscriberID = models.IntegerField(primary_key=True)
	username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
	subscriptionTypeCode = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
	serviceCode = models.ForeignKey(Service, on_delete=models.CASCADE)
	requestDate = models.DateField()
	startDate = models.DateField()
	endDate = models.DateField()
	motifOfCancellation = models.TextField()

	def __str__(self):
		return self.username.username




class TransferredSubscription(models.Model):
	transferID = models.IntegerField(primary_key=True)

	transferFrom = models.CharField(max_length=20)
	transferTo = models.CharField(max_length=20)
	requestDate = models.DateField()
	transferDate = models.DateField()
	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

	def __str__(self):
		return self.transferID



class Office(models.Model):
	officeCode = models.IntegerField(primary_key=True)
	officeName = models.CharField(max_length=20)
	attribution = models.CharField(max_length=20)

	def __str__(self):
		return self.officeCode


class Officer(models.Model):
	officeCode = models.ForeignKey(Office, on_delete=models.CASCADE)
	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()

	def __str__(self):
		return self.officeCode.officeCode




class Organization(models.Model):
	organizationCode = models.IntegerField(primary_key=True)
	organizationName = models.CharField(max_length=20)
	description = models.TextField()
	dateJoined = models.DateField()
	address1 = models.CharField(max_length=20)
	address2 = models.CharField(max_length=20)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=20)
	phoneNumber = models.CharField(max_length=20)

	def __str__(self):
		return self.organizationName



class OrganizationMember(models.Model):
	organizationCode = models.ForeignKey(Organization, on_delete=models.CASCADE)
	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	startDate = models.DateField(max_length=20)
	endDate = models.DateField(max_length=20)
	nativeCountry = models.CharField(max_length=20)
	citizenship = models.CharField(max_length=20)
	isDelegate = models.BooleanField()

	def __str__(self):
		return self.organizationCode.organizationCode





