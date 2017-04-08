from django import forms
import re

def validate_username(value):
	if not re.match(r'^([A-z0-9]{1,}[A-z0-9-]{4,})$', value):
		raise forms.ValidationError("Username must allow only letters, numbers and dashes (-). It must also be at least 5 characters long.")


def validate_password(value):
	if not re.match(r'^[A-z0-9-^_$/\\]{4,}$', value):
		raise forms.ValidationError("The password must be at least 4 characters long.  A-z, 0-9, ^, -, _, $, /, \\")


def validate_transaction_name(value):
	if not re.match(r'^([A-z0-9]{1,}[A-z0-9- ]*$)', value):
		raise forms.ValidationError("Name must be at least one letter/number. Dashes and Spaces are accepted as complement.")


def validate_category_name(value):
	if not re.match(r'^([A-z0-9]{1,}[A-z0-9 ]*$)', value):
		raise forms.ValidationError("Name must be at least one letter/number. Spaces are accepted as complement.")
