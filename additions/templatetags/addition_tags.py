from django import template
from ..models import Partners

register = template.Library()

@register.inclusion_tag('template_tags/partners_list.html')
def list_partners(count=10):
	partners = Partners.objects.filter(is_active=True)
	return {'partners':partners}
