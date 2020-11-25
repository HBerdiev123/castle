from django import forms 
from .models import Emails, EmailToAgent, ReplyLetter

class ContactForm(forms.ModelForm):
	class Meta:
		model   = Emails
		exclude = ('created_at', 'updated_at', 'is_checked')

class AgentForm(forms.ModelForm):
	class Meta:
		model   = EmailToAgent
		exclude = ('created_at', 'updated_at', 'is_checked')
		widgets = {'agent': forms.HiddenInput()}	

class ReplyForm(forms.ModelForm):
	class Meta:
		model   = ReplyLetter
		exclude = ('created_at', 'updated_at')		
		widgets  = {
				    'sender': forms.HiddenInput(), 
				    'email':forms.HiddenInput(),
				    'agent':forms.HiddenInput(),
				   }		