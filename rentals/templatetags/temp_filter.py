from rentals.models import  Properties, PropertyCategory, PROPERTY_PURPOSE, Message
from rentals.models import Picture
from django import template

register = template.Library()

@register.filter(name='getbyidproperty')
def getbyid_property(pk):
	property_image=Picture.objects.filter(properties=pk).first()
	image=property_image
	return image.picture


@register.filter(name='getunreadmessages')
def getunreadmessages(val):
	message=Message.objects.filter(status="0").count()
	return message



@register.filter(name='getpropertycategory')
def get_category(pk):
	property_category=PropertyCategory.objects.get(id=pk)
	category=property_category.title
	return category

@register.filter(name='getselectedfieldname')
def selected_choice(field_name):
    return PROPERTY_PURPOSE[int(field_name)][1]

@register.filter(name='getunreadmessages')
def getunreadmessages(val):
	message=Message.objects.all().filter().count()
	return message

# @register.filter(name='getimages')
# def getimages(id):
# 	images=Picture.objects.filter(properties=id)
# 	return images


@register.filter(name='getall')
def allproperties(pk):
	all_properties=Properties.objects.allproperties().count()
	
	return  all_properties

@register.filter(name='getactiveproperties')
def activeproperties(pk):
	active_properties=Properties.objects.all().count()
	
	return active_properties


@register.filter(name='propertiesforsale')
def saleproperties(pk):
	properties=Properties.objects.all().filter(purpose='1').count()
	return properties

@register.filter(name='propertiesforrent')
def rentproperties(pk):
	properties=Properties.objects.all().filter(purpose='0').count()
	return properties