from django import forms 
from .models import Emails, EmailToAgent, ReplyLetter
from django.forms import ModelForm
from .models import ContactNumber, SocialContact, ContactAddress, ContactEmail, MessageEmail, TwilloContact


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

class ContactNumberForm(forms.ModelForm):

	class Meta:
		model = ContactNumber
		fields = '__all__'

class SocialContactForm(forms.ModelForm):

	class Meta:
		model = SocialContact
		fields = '__all__'

class ContactAddressForm(forms.ModelForm):

	class Meta:
		model = ContactAddress
		fields = '__all__'

class ContactEmailForm(forms.ModelForm):

	class Meta:
		model = ContactEmail
		fields = '__all__'


class MessageEmailForm(forms.ModelForm):

	class Meta:
		model = MessageEmail
		fields = '__all__'

class TwilloContactForm(forms.ModelForm):

	class Meta:
		model = TwilloContact
		fields = '__all__'

