from django.db import models
from django.conf import settings 
from property.models import Property


# Create your models here.

class Profile(models.Model):
	user          = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
	date_of_birth = models.DateField(blank=True, null=True)
	mobile	      = models.CharField(max_length=20)
	photo	      = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)
	about 		  = models.TextField(blank=True)
	my_favorities = models.ManyToManyField(Property, related_name='user_liked', blank=True)

	# def __str__(self):
	# 	return f'Profile for user {self.user.username}'

class Team(Profile):
	priority   = models.IntegerField()
	occupation = models.CharField(max_length=30)
	created_at = models.DateField(auto_now_add=True)
	update_at  = models.DateField(auto_now=True)

	# def __str__(self):
	# 	return self.user

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = 'Team Members'



# class MyFavorites(models.Model):
# 	user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# 	appartment   = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True, null=True)
# 	created_at   = models.DateTimeField(auto_now_add=True)
# 	updated_at   = models.DateTimeField(auto_now=True)


	# def __str__(self):
	# 	return self.user.username