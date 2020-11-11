from django.db import models

# Create your models here.


class FAQ(models.Model):
	title	   = models.CharField(max_length=120)
	body  	   = models.TextField()
	is_active  = models.BooleanField(default=True)
	priority   = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'FAQs'
		ordering            = ['priority']

class Partners(models.Model):
	partner_name = models.CharField(max_length=120)
	partner_url  = models.URLField()
	logo  		 = models.ImageField(upload_to='partners')
	priority     = models.IntegerField()
	is_active    = models.BooleanField(default=True)
	created_at   = models.DateField(auto_now_add=True)
	updated_at   = models.DateField(auto_now=True)

	def __str__(self):
		return self.partner_name

	class Meta:
		verbose_name_plural = 'Partners'
		ordering            = ['priority']	