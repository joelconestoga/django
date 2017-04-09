from django.contrib.auth.models import User
from django import forms
from .models import Transaction, Category
from .validators import *

class RegisterForm(forms.ModelForm):

	username = forms.CharField(validators=[validate_username])
	password = forms.CharField(validators=[validate_password], widget=forms.PasswordInput)
	confirmation = forms.CharField(widget=forms.PasswordInput);

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def clean(self):
		password = self.cleaned_data.get('password')
		confirmation = self.cleaned_data.get('confirmation')

		if password and password != confirmation:
			self.add_error("password", "Passwords don't match.")


class TransactionForm(forms.ModelForm):

	name = forms.CharField(validators=[validate_transaction_name])

	class Meta:
		model = Transaction
		fields = ['name', 'value', 'category']


class CategoryForm(forms.ModelForm):

	name = forms.CharField(validators=[validate_category_name])

	class Meta:
		model = Category
		fields = ['name']
