from django import template
from ..models import FeaturedProperties

register = template.Library()

@register.inclusion_tag('template_tags/featured.html')
def featured(count=10):
	featured =FeaturedProperties.objects.filter(is_active=True)[:10]
	return {'featured': featured}
