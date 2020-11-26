from rentals.models import Message
from rentals.models import PropertyCategory, PROPERTY_PURPOSE, Properties



# register = template.Library()

# @register.filter(name='getunreadmessages')
# def getunreadmessages(val):
# 	message=Message.objects.all().filter().count()
# 	return message




@register.filter(name='getpropertycategory')
def get_category(pk):
	property_category=PropertyCategory.objects.get(id=pk)
	category=property_category.title
	return category

@register.filter(name='getselectedfieldname')
def selected_choice(field_name):
    return PROPERTY_PURPOSE[int(field_name)][1]


@register.filter(name='getusername')
def getusername(field_name):
    return PROPERTY_PURPOSE[int(field_name)][1]


request.user.get_username()