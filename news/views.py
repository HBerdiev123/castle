from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Count
from .forms import SearchForm
# Create your views here.

def detail(request, slug):
	post  = get_object_or_404(Post, slug=slug)
	post_tag_ids = post.tags.values_list('id', flat=True)
	similar_posts= Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
	similar_posts= similar_posts.annotate(same_tags=Count('tags'))\
	.order_by('-same_tags', '-publish')[:3]
	return render(request,'news/news_details.html',{'post':post, 'similar_posts':similar_posts})


def list(request, tag_slug=None, cat_slug=None):
	object_list     = Post.published.all()
	cats            = Category.objects.all()

	if cat_slug:
		category    = get_object_or_404(Category, slug=cat_slug)
		object_list = object_list.filter(post_category=category)

	if tag_slug:
		tag 		= get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags__in=[tag])

	page 	  = request.GET.get('page')
	paginator = Paginator(object_list, 1)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'news/news_list.html',{'posts':posts, 'page':page, 'cats':cats})	


def post_search(request):
	form = SearchForm()
	query = None
	print(request.POST)
	results = []
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			query = form.cleaned_data['query']
			search_vector = SearchVector('title', weight='A')+\
			SearchVector('body', weight='B')
			search_query  = SearchQuery(query)
			results = Post.published.annotate(search=search_vector, rank = SearchRank(search_vector, search_query))\
			.filter(search=search_query).order_by('-rank')
	return render(request, 'news/search_result.html', {'form':form, 'query':query, 'results':results})

