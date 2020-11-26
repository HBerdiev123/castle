from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Emails(models.Model):
	sender       = models.CharField(max_length=50)
	email        = models.EmailField()
	message      = models.TextField()
	created_at   = models.DateTimeField(auto_now_add=True)
	updated_at   = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'A message by {} at {}'.format(self.sender, self.created_at)


class EmailToAgent(Emails):
	agent        = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	is_checked   = models.BooleanField(default=False)
	is_replied   = models.BooleanField(default=False)

class ReplyLetter(Emails):
	agent        = models.ForeignKey(User, on_delete = models.CASCADE)


class ContactNumber(models.Model):
	title         =models.CharField(max_length=100)
	contact_number=models.CharField(max_length=25)
	created 	  =models.DateTimeField(auto_now=True)


class SocialContact(models.Model):
	title         =models.CharField(max_length=25)
	social_url    =models.CharField(max_length=150)
	social_icon   =models.CharField(max_length=150, blank=True)
	created 	  =models.DateTimeField(auto_now=True)


class ContactAddress(models.Model):
	title       =models.CharField(max_length=100)
	address     =models.CharField(max_length=255)
	city		=models.CharField(max_length=255, blank=True)	
	region		=models.CharField(max_length=255, blank=True)
	country		=models.CharField(max_length=255, blank=True)
	postalcode	=models.CharField(max_length=50)
	latitude    =models.DecimalField(max_digits=22, decimal_places=16)
	longitude   =models.DecimalField(max_digits=22, decimal_places=16)
	created 	=models.DateTimeField(auto_now=True)

	

class ContactEmail(models.Model):
	title         =models.CharField(max_length=100)
	email         =models.CharField(max_length=100)
	created 	  =models.DateTimeField(auto_now=True)


class MessageEmail(models.Model):
	title             =models.CharField(max_length=100)
	message_email     =models.CharField(max_length=100)
	email_host        =models.CharField(max_length=100)
	email_port        =models.CharField(max_length=100)
	created 	      =models.DateTimeField(auto_now=True)



class TwilloContact(models.Model):
	title          =models.CharField(max_length=100)
	user           =models.ManyToManyField(User, blank=True)
	twillo_account =models.CharField(max_length=100)
	twillo_token   =models.CharField(max_length=100)
	twillo_number  =models.CharField(max_length=100)
	default_twillo =models.CharField(max_length=100, blank=True, default=False)
	created 	   =models.DateTimeField(auto_now=True)

