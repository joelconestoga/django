from django.contrib.auth.models import User
from django import forms
from .models import Transaction, Category

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']


class TransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = ['name', 'value', 'category']


class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ['name']
