from django import forms
from Users.models import User

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['full_name', 'email', 'password', 'mobile', 'address']
