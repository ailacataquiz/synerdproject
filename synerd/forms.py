from django import forms

class JoinUsForm(forms.Form):
	username = forms.CharField(max_length=20, 
		widget=forms.TextInput(attrs={'placeholder':'Required'}))
	password = forms.CharField(max_length=20,
		widget=forms.TextInput(attrs={'placeholder':'Required'}))
	firstname = forms.CharField(max_length=20,
		widget=forms.TextInput())
	middlename = forms.CharField(max_length=20,
		widget=forms.TextInput())
	lastname = forms.CharField(max_length=20,
		widget=forms.TextInput())

	address1 = forms.CharField(max_length=20,
		widget=forms.TextInput())
	address2 = forms.CharField(max_length=20,
		widget=forms.TextInput())
	city = forms.CharField(max_length=20,
		widget=forms.TextInput())
	state = forms.CharField(max_length=20,
		widget=forms.TextInput())
	zipcode = forms.CharField(max_length=20,
		widget=forms.TextInput())

	email = forms.EmailField(max_length=20,
		widget=forms.TextInput())
	phonenumber = forms.CharField(max_length=20,
		widget=forms.TextInput())

	dob = forms.DateField()

class SignInForm(forms.Form):
	username = forms.CharField(max_length=20,
		widget=forms.TextInput())
	password = forms.CharField(max_length=20,
		widget=forms.PasswordInput())


