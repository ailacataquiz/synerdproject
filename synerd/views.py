from django.shortcuts import render, redirect
from .models import Service, Subscriber, Organization, UserInfo
from .forms import JoinUsForm, SignInForm
from .filters import UserInfoFilter
from django.urls import reverse 
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def home(request):
	return render(request, 'synerd/home.html')

def signin(request):
	if request.method == 'POST':
		signInForm = SignInForm(request.POST)
		if signInForm.is_valid():
			new_data = UserInfo(username=request.POST['username'])
			new_data.save()
			return redirect('signInForm')
	else:	
		signInForm = SignInForm()
	
	context = {'signInForm' : signInForm}
	return render(request, 'synerd/signin.html', context)


def form(request):
	if request.method == 'POST':
		form = JoinUsForm(request.POST)

		if form.is_valid():
			new_data = UserInfo(username=request.POST['username'],
								firstName=request.POST['firstname'],
								middleName=request.POST['middlename'],
								lastName=request.POST['lastname'],
								address1=request.POST['address1'],
								address2=request.POST['address2'],
								city=request.POST['city'],
								state=request.POST['state'],
								zipcode=request.POST['zipcode'],
								)
			new_data.save()
			return redirect('form')
	else:	
		form = JoinUsForm()
	
	context = {'form' : form}
	return render(request, 'synerd/form.html', context)

def otherform(request):
	return render(request, 'synerd/otherform.html')

def members(request):
	query_subscriber = Subscriber.objects.all()
	myFilter = UserInfoFilter(request.GET, queryset=query_subscriber)
	query_subscriber = myFilter.qs

	context = {'query_subscriber' : query_subscriber, 'myFilter':myFilter}

	return render(request, 'synerd/members.html', context)