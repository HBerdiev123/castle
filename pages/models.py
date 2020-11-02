from django.db import models
from django.conf import settings 
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.
class Page(models.Model):
	title 	   = models.CharField(max_length=255)
	slug  	   = models.SlugField()
	body  	   = RichTextUploadingField()
	author 	   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at  = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('page', args=[self.slug])