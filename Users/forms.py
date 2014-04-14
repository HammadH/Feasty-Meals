from django import forms
from django.contrib.auth.forms import AuthenticationForm

from Users.models import User


PACKAGE_TYPE = (('Indian','Indian'),
				('Pakistani','Pakistani'),
				('Mixed','MIXED'),)


class AuthForm(AuthenticationForm):
	username = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}), max_length=254, label='')
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	address = forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))
	free_meal_package = forms.ChoiceField(choices=PACKAGE_TYPE, widget=forms.RadioSelect())
	class Meta:
		model = User
		fields = ['full_name', 'email', 'password', 'free_meal_package' ,'mobile', 'address']


