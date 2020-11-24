from django import forms 
from .models import Emails, EmailToAgent

class ContactForm(forms.ModelForm):
	class Meta:
		model = Emails
		exclude = ('created_at', 'updated_at', 'is_checked')

class AgentForm(forms.ModelForm):
	class Meta:
		model = EmailToAgent
		exclude = ('created_at', 'updated_at', 'is_checked')	