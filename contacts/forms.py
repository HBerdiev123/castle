from django import forms 
from .models import Emails

class ContactForm(forms.ModelForm):
	class Meta:
		model = Emails
		exclude = ('created_at', 'updated_at', 'is_checked')