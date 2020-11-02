from django import template
from ..models import Post 
from ..models import Category

register = template.Library()

@register.inclusion_tag('template_tags/recent_posts.html')
def recent_posts(count=3):
	latest_posts = Post.objects.filter(status='published')[:count]
	return {'latest_posts':latest_posts}


@register.inclusion_tag('template_tags/post_categories.html')
def show_categories(count=10):
	cats = Category.objects.all()[:count]
	return {'cats':cats}


@register.inclusion_tag('template_tags/recent_posts.html')
def featured_properties(count=4):
	pass	
