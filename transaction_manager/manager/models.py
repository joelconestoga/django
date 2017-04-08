from django.contrib.auth.models import User
from django.db import models
from .validators import validate_transaction_name, validate_category_name

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50, validators=[validate_category_name])

	def __str__(self):
		return self.name
		

class Transaction(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100, validators=[validate_transaction_name])
	value = models.DecimalField(max_digits=6, decimal_places=2)
	category = models.ForeignKey(Category, default=1)

	def __str__(self):
		return self.name + ' - ' + str(self.value)


