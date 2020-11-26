from django import forms
from .models import Message


class SearchForm(forms.Form):
	query 		  =forms.CharField(required=False)
	min_bed		  =forms.IntegerField(required=False)
	min_bath      =forms.IntegerField(required=False)
	min_area	  =forms.DecimalField(required=False)
	max_area      =forms.DecimalField(required=False)
	available_from=forms.DateField(required=False)
	location      =forms.CharField(required=False)
	category      =forms.IntegerField(required=False)
	min_price     =forms.IntegerField(required=False)
	max_price     =forms.IntegerField(required=False)
	purpose		  =forms.CharField(required=False)



# class MessageForm(forms.Form):
# 	full_name	   =forms.CharField(max_length=255)
# 	phone_number   =forms.CharField(max_length=17, required=False)
# 	email          =forms.EmailField()
# 	message        =forms.CharField(widget=forms.Textarea)
# 	properties     =forms.CharField(required=False)
	


class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		# fields="__all__"
		fields=['full_name', 'phone_number', 'email', 'message', 'properties']

	
	