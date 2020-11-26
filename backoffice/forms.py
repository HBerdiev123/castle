from django import forms
from rentals.models import Feature, ReplyMessage, Properties, Picture, PropertyCategory
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from djrichtextfield.widgets import RichTextWidget
from django.db import models
from ckeditor.fields import RichTextField




class SearchMessage(forms.Form):
	query 		  =forms.CharField(required=False)
	start_date    =forms.DateField(required=False)
	end_date	  =forms.DateField(required=False)
	phone_number  =forms.CharField(required=False)
	status		  =forms.CharField(required=False)
	


class PropertyForm(forms.ModelForm):
	# description = forms.CharField(widget=CKEditorWidget())
	# bathroom = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Properties
		fields = ['title', 'size', 'price','bedroom', 'bathroom', 'available_from', 'status', 'purpose', 'category', 'year_built', 'garage', 'floor', 'total_floor', 'internet', 'house_number', 'street', 'city', 'region', 'postal_Code', 'country', 'latitude', 'longitude', 'description', 'feature', 'pet_policy',  'featured']
		widgets = {
			'feature' : forms.CheckboxSelectMultiple(), 
			'description':forms.CharField(widget=RichTextWidget()),  
		}
	# def __init__(self, *args, **kwargs):
	# 	super(PropertyForm, self).__init__(*args, **kwargs)
	# 	self.fields['bathroom'].widget.attrs['class'] = 'form-control'

# AddressFormSet=inlineformset_factory(Address, Property, can_delete=True, form=AddressForm)
# PropertyFormSet = inlineformset_factory(Address, Property, form=PropertyForm, max_num=1)

from django.forms import ClearableFileInput


class ReplyMessageForm(forms.ModelForm):
	class Meta:
		model=ReplyMessage
		fields=['title', 'reply_message', 'message']
		# fields='__all__'
# forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
class PictureForm(forms.ModelForm):
	# picture = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model=Picture
		fields = ['picture']
		widgets = {
			'picture' : forms.ClearableFileInput(attrs={'multiple': True}), 
		}
# from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class PropertyPicture(forms.ModelForm):
	# picture=MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
	# picture = forms.CharField(widget=CKEditorUploadingWidget())

	class Meta:
		model=Picture
		fields='__all__'
		# widgets = {
  #           'picture': ClearableFileInput(attrs={'multiple': True}),
  #       }
		# widgets = {
		# 	'picture' : forms.FileField(widget=widgets.FineUploaderWidget)
		# }




class FeatureForm(forms.ModelForm):
	class Meta:
		model=Feature
		fields='__all__'


# from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class PropertyCategoryForm(forms.ModelForm):
	class Meta:
		model=PropertyCategory
		fields='__all__'
		# widgets = {
		# 	'picture' : MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)
		# }
		# attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

# If you need to upload media files, you can use this:


