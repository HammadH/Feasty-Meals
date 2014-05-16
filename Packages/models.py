import os
import datetime

from django.db import models
from django.contrib import admin
from sorl.thumbnail import ImageField





PACKAGE_BILLING_TYPE = (('1W', '1 Week'),
						('2W', '2 Weeks'),
						('3W', '3 Weeks'),
						('1M', '1 Month'))
						
PAYMENT_STATUS = (('1','PAID'),
				  ('0','NOT-PAID'))

# MENU_TYPE = ('I':'Indian',
# 			 'P':'Pakistani')

def get_promo_image_path(instance, filename):
	return os.path.join('Promotion', '%s' %instance, '%s' %filename)

def get_mealitem_image_path(instance, filename):
	return os.path.join('MealItemImages', '%s' %instance, '%s' %filename)


class Promotion(models.Model):
	name = models.CharField(max_length=50, unique=True)
	is_active = models.BooleanField(default=False)
	date = models.DateTimeField(blank=True, null=True)
	image = models.ImageField(upload_to=get_promo_image_path)

	def __unicode__(self):
		return self.name







class Package(models.Model):
	name=models.CharField(blank=False, null=True, max_length=70)

	def __unicode__(self):
		return self.name

class PaymentManager(models.Manager):
	def create(self, user, package):
		self.user = user
		self.package = package
		self.save()
		self._expires_on = self.purchased_on + datetime.timedelta(days=7)
		self.save()
		return self

class Payment(models.Model):
	from Users.models import User
	user = models.ForeignKey(User, related_name='payment')
	package = models.ForeignKey(Package)
	has_paid = models.BooleanField(default=False)
	purchased_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	renewed_on = models.DateTimeField(blank=True, null=True)

	is_cancelled =  models.BooleanField(default=False)
	_expires_on = models.DateTimeField(null=True, blank=True)

	objects = PaymentManager()

	def __unicode__(self):
		return self.user.full_name

	@property
	def is_active(self):
		if has_paid and not is_cancelled:
			return True
		else:
			return False
	
	@property
	def expires_on(self):
	    return self._expires_on

class Meal(models.Model):

	name = models.CharField(max_length=70)
	package = models.ForeignKey(Package)

	def __unicode__(self):
		return self.name


class MealItem(models.Model):
	pic = ImageField(upload_to=get_mealitem_image_path)
	name = models.CharField(max_length=70)
	meal = models.ForeignKey(Meal)

	def __unicode__(self):
		return self.name




	    

admin.site.register(Meal)
admin.site.register(MealItem)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(Promotion)
# class Menu(models.Model):
# 	menu_type = models.ChoiceField()


# class Meal(models.Model):
# 	name = models.CharField(max_length=100, blank=False)
    














