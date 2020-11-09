from django.db import models

# Create your models here.
class Emails(models.Model):
	sender     = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20, blank=True, null=True)
	email      = models.EmailField()
	message    = models.TextField()
	is_checked = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'A message by {} at {}'.format(self.sender, self.created_at)