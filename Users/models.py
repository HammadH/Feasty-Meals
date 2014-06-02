import logging

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import signals
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string

from Packages.models import Package



class UserManager(BaseUserManager):
	def create_user(self, full_name, meal_package, email, password, mobile, area, building, room):
			new_user = self.model(full_name=full_name, email=email, meal_package=meal_package,
								mobile=mobile, area_name=area, building_name=building, room_no=room)
			new_user.set_password(password)

			try:
				new_user.save()
				return new_user
			except Exception, e:
				print e 
				return None
					
	def create_superuser(self, email, password, mobile):
		new_user = self.model(email=email)
		new_user.set_password(password)
		new_user.mobile = mobile
		new_user.is_superuser = True
		new_user.save()
		return new_user

	def activate_user(self, user):
		user.is_active=True
		#send signal to me 
		user.save()
		return True

 # send_mail(subject, message, from_email, recipient_list, fail_silently=False, 
 # 	auth_user=None, auth_password=None, connection=None, html_message=None)
	
	
	def user_registered_notification_email(self, superuser, user):
		pass

	def user_activated_notification_email(self, superuser, user):
		pass


class User(AbstractBaseUser, PermissionsMixin):
	full_name = models.CharField(max_length=100, blank=False)
	email = models.EmailField(unique=True, blank=False)
	meal_package = models.ForeignKey(Package, null=True, blank=False)
	mobile = models.CharField(unique=True, blank=False, max_length=10)
	area_name = models.TextField(blank=False, null=True, max_length=70)
	building_name = models.TextField(blank=False, null=True, max_length=70)
	room_no = models.TextField(blank=False, null=True, max_length=70)


	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['mobile']
	objects = UserManager()

	def __unicode__(self):
		return self.full_name

	def get_full_name(self):
		return self.full_name

	def get_short_name(self):
		return self.full_name

	def get_mobile(self):
		return self.mobile

	def get_address(self):
		return self.address

	def get_email(self):
		return self.email

	def has_package(self):
		if self.meal_package:
			return True
		else: return False

	def get_package(self):
		if self.package.get():
			return self.package.get()
		else:
			return None

	def is_package_active(self):
		if self.package.get().payment_status == 1:
			return True
		else: return False


def send_emails(sender, instance, created, **kwargs):
		if created:
			subject = "New Registration"
			message = render_to_string('email_message.html', {'user':instance})
			from_email = "eat@ichdubai.com"                 #common email to send out emails from feastymeals
			recipient_list = ['registrations@ichdubai.com, wishmecake@gmail.com']   #this will be my email for user infos
			
			subject_to_user = "Hello there!"
			message_to_user = render_to_string('user_email_message.html', {'user':instance})
			recipient_user = [instance.email]
			try:
				send_mail(subject, message, from_email, recipient_list)
				send_mail(subject_to_user, message_to_user, from_email, recipient_user )
				
			except Exception, e:
				logging.basicConfig(filename='feasty_email_logs.log', level=logging.DEBUG)
				logging.debug(e)
				

				
				
		else:
			return
		




signals.post_save.connect(send_emails, User, dispatch_uid= "new user registration")




admin.site.register(User)


