import os

from django.db import models
from django.contrib import admin





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





admin.site.register(Package)
admin.site.register(Promotion)
# class Menu(models.Model):
# 	menu_type = models.ChoiceField()


# class Meal(models.Model):
# 	name = models.CharField(max_length=100, blank=False)
    














