from django.db import models
from django.conf import settings 
from property.models import Property

# Create your models here.

class Profile(models.Model):
	user          = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	mobile	      = models.CharField(max_length=20)
	photo	      = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
	about 		  = models.TextField(blank=True)
	my_favorities = models.ManyToManyField(Property, related_name='user_liked')

	# def __str__(self):
	# 	return f'Profile for user {self.user.username}'


# class MyFavorites(models.Model):
# 	user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# 	appartment   = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
# 	created_at   = models.DateTimeField(auto_now_add=True)
# 	updated_at   = models.DateTimeField(auto_now=True)


	# def __str__(self):
	# 	return self.user.username