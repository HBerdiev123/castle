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
