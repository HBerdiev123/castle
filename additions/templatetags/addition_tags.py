from django import template
from ..models import Partners
from ..models import Testimonal

register = template.Library()

@register.inclusion_tag('template_tags/partners_list12.html')
def list_partners(count=10):
	partners = Partners.objects.filter(is_active=True)
	return {'partners':partners}

@register.inclusion_tag('template_tags/partners_list.html')
def list_partners(count=20):
	partners = Partners.objects.filter(is_active=True)
	return {'partners':partners}

@register.inclusion_tag('template_tags/happy_customers.html')
def show_happy_customer(count=4):
	customers = Testimonal.objects.filter(is_active=True)
	return {'customers':customers}