from django.shortcuts import render
from .models import  Properties, PropertyCategory, Picture
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import SearchForm, MessageForm
from django.contrib.postgres.search import TrigramSimilarity
from django import template
from django.db.models.functions import Greatest
from django.http import HttpResponse

# Create your views here.


def max_min_price(purpose):
	max_price=None
	min_price=None

	if purpose==0:
		max_price=Properties.objects.max_rent_price()
		min_price=Properties.objects.min_rent_price()
	elif purpose==1:
		max_price=Properties.objects.max_sale_price()
		min_price=Properties.objects.min_sale_price()
	else:
		max_price=Properties.objects.max_price()
		min_price=Properties.objects.min_price()
	return max_price, min_price





def property_search(request):
	form = SearchForm()
	properties=Properties.objects.all()
	property_category=PropertyCategory.objects.all()
	property_purpose=Properties.PROPERTY_PURPOSE
	max_rent=Properties.objects.max_rent_price()
	min_rent=Properties.objects.min_rent_price()
	
	query = None
	min_bed=None
	min_bath=None
	max_area=None
	min_area=None
	available_from=None
	location=None
	category=None
	min_price=None
	max_price=None
	purpose=None
	results = []
	if request.method=="GET":
		form = SearchForm(request.GET)
		if form.is_valid():
			query 		  =form.cleaned_data['query']
			min_bed       =form.cleaned_data['min_bed']
			min_bath	  =form.cleaned_data['min_bath']
			min_area	  =form.cleaned_data['min_area']
			max_area	  =form.cleaned_data['max_area']
			available_from=form.cleaned_data['available_from']
			location      =form.cleaned_data['location']
			
			category      =form.cleaned_data['category']
			min_price 	  =form.cleaned_data['min_price']
			max_price     =form.cleaned_data['max_price']
			purpose       =form.cleaned_data['purpose']

			
			results 	= Properties.objects.all()
			if query:
				results=results.annotate(similarity=Greatest(TrigramSimilarity("title", query), TrigramSimilarity("description", query), 
					TrigramSimilarity("street", query), TrigramSimilarity("city", query), TrigramSimilarity("region", query), TrigramSimilarity("country", query),
					)).filter(similarity__gt=0.1).order_by('-similarity')
			# if location:
			# 	result=results.filter(city=location)
			
			if min_bed:
				results=results.filter(bedroom__gte=min_bed)
			if category:
				results=results.filter(category=category)
			if min_bath:
				results=results.filter(bathroom__gte=min_bath)
			if min_area:
				results=results.filter(size__gte=min_area)
			if max_area:
				results=results.filter(size__lte=max_area)
			if available_from:
				results=results.filter(available_from__gte=available_from)
			if min_price:
				results=results.filter(price__gte=min_price)
			if max_price:
				results=results.filter(price__lte=max_price)
			if purpose:
				results=results.filter(purpose=purpose)
			if location:
				results=results.annotate(similarity=Greatest(TrigramSimilarity("street", location), TrigramSimilarity("city", location), TrigramSimilarity("region", location), TrigramSimilarity("country", location),
					)).filter(similarity__gt=0.1).order_by('-similarity')

			if not query and not min_bed and not category and not min_bath and not min_area and not max_area and not available_from and not location and not min_price and not max_price and not purpose:
				results 	= Properties.objects.all()
				
			
		
			# results 	= Property.objects.active_status().annotate(similarity=TrigramSimilarity("title", query),
			# 	).filter(similarity__gt=0.1, bedroom__gte=min_bed, bathroom__gte=min_bath, size__gte=min_area, size__lte=max_area).order_by('-similarity')
	else:
		form = SearchForm()

	# page = request.GET.get('page', None)
	# paginator = Paginator(results, 10)
	# try:
	# 	visable_area_properties = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer deliver the first page
	# 	visable_area_properties = paginator.page(1)
	# except EmptyPage:
	# 	visable_area_properties = paginator.page(paginator.num_pages)

	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"available_from":available_from,
		'category':category,
		'purpose':purpose,
		'location':location,
		'max_rent_price':max_rent,
	    'min_rent_price':min_rent,
	    'min_price':min_price,
		'max_price':max_price,

		# 'visable_area_properties':visable_area_properties,
		'all_properties': results,
		'property':properties,
		'property_category':property_category,
		'property_purpose':property_purpose,
	}

	return render(request, 'listing/listing4.html', context)

def rent_list(request):

	property_category=PropertyCategory.objects.all()
	property_purpose=Properties.PROPERTY_PURPOSE
	category=None
	purpose=None

	all_properties=Properties.objects.all()
	number_of_properties=Properties.objects.count()
	max_rent=Properties.objects.max_rent_price()
	min_rent=Properties.objects.min_rent_price()
	page = request.GET.get('page', None)
	paginator = Paginator(all_properties, 10)
	try:
		visable_area_properties = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		visable_area_properties = paginator.page(1)
	except EmptyPage:
		visable_area_properties = paginator.page(paginator.num_pages)
	context={
	'number_of_properties':number_of_properties,
	'max_rent_price':max_rent,
	'min_rent_price':min_rent,
	'property_category':property_category,
	'property_purpose':property_purpose,
	'category':category,
	'purpose':purpose,

	'all_properties':all_properties, 
	'visable_area_properties':visable_area_properties,
	

	}
	
	return render(request, 'listing/listing4.html', context)	






def load_coordinates(request):
	query = None
	min_bed=None
	min_bath=None
	max_area=None
	min_area=None
	available_from=None
	location=None
	category=None
	min_price=None
	max_price=None
	purpose=None
	visable_area_properties = []
	if request.method == 'GET':
		get_coordinates=request.GET.get('borders')
		query=request.GET.get('query')
		min_bed=request.GET.get('min_bed')
		min_bath=request.GET.get('min_bath')
		min_area=request.GET.get('min_area')
		max_area=request.GET.get('max_area')
		category=request.GET.get('property_category')
		purpose=request.GET.get('property_purpose')
		location=request.GET.get('location')
		min_price=request.GET.get('min_price')
		max_price=request.GET.get('max_price')
		lists=json.loads(get_coordinates)
		latitude1=lists[0][0]
		latitude2=lists[1][0]
		longitude1=lists[0][1]
		longitude2=lists[1][1]
		visable_area_properties=Properties.objects.filter(status='1').filter(latitude__range=(latitude1, latitude2), longitude__range=(longitude1, longitude2))
		if query:
				visable_area_properties=visable_area_properties.annotate(similarity=Greatest(TrigramSimilarity("title", query), TrigramSimilarity("description", query), 
					TrigramSimilarity("street", query), TrigramSimilarity("city", query), TrigramSimilarity("region", query), TrigramSimilarity("country", query),
					)).filter(similarity__gt=0.1).order_by('-similarity')
		# if location:
		# 	visable_area_properties=visable_area_properties.filter(location=location)
		if min_bed:
			visable_area_properties=visable_area_properties.filter(bedroom__gte=min_bed)
		if category:
			visable_area_properties=visable_area_properties.filter(category=category)
		if min_bath:
			visable_area_properties=visable_area_properties.filter(bathroom__gte=min_bath)
		if min_area:
			visable_area_properties=visable_area_properties.filter(size__gte=min_area)
		if max_area:
			visable_area_properties=visable_area_properties.filter(size__lte=max_area)
		if available_from:
			visable_area_properties=visable_area_properties.filter(available_from__gte=available_from)
		if min_price:
			visable_area_properties=visable_area_properties.filter(price__gte=min_price)
		if max_price:
			visable_area_properties=visable_area_properties.filter(price__lte=max_price)
		if purpose:
			visable_area_properties=visable_area_properties.filter(purpose=purpose)

		if location:
			visable_area_properties=visable_area_properties.annotate(similarity=Greatest(TrigramSimilarity("street", location), TrigramSimilarity("city", location), TrigramSimilarity("region", location), TrigramSimilarity("country", location),
				)).filter(similarity__gt=0.1).order_by('-similarity')


	page = request.GET.get('page_n', None)
	paginator = Paginator(visable_area_properties, 10) 
	first_page=paginator.page(1).object_list
	page_range=paginator.page_range
	try:
		visable_area_properties = paginator.page(page)
	except PageNotAnInteger:
		visable_area_properties = paginator.page(1)
	except EmptyPage:
		visable_area_properties = paginator.page(paginator.num_pages)
	context={
	'first_page':first_page,
	'page_ranges':page_range,
	'visable_area_properties':visable_area_properties,
	}

		# if request.method == 'POST':
		# 	page_n = request.POST.get('page_n', None) #getting page number
		# 	results = list(paginator.page(page_n).object_list.values('id'))
		# 	return JsonResponse({"address":results})
	
	return render(request, 'rentals/properties.html', context)




def rent_detail(request, id=None, *args, **kwargs):
	try:
		home=Properties.objects.active_status().get(id=id)
		images=Picture.objects.filter(properties=id)
	except Properties.DoesNotExist:
		raise Http404("Property does not exist")

	new_message=None
	if request.method=="POST":
		message_form=MessageForm(request.POST)
		if message_form.is_valid() and not request.is_ajax():
			new_message=message_form.save(commit=False)
			# new_message.properties=home
			new_message.save()
			data = {'status':'saved'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		message_form=MessageForm()
			
	context={
		'property':home,
		'new_message':new_message,
		'images':images,
		'message_form':message_form,
		}
	return render(request, 'listing/property_detail1.html', context)






def getbyid_property(request):
	if request.method=='GET':
		get_id=request.GET.get('pk')
		property_detail=Properties.objects.active_status().get(id=get_id)
		return render(request, 'listing/snippets/property_detail_map.html', {'property_detail':property_detail})



def rent(request):
	return render(request, 'profile/property_detail1.html', {})

def delete_js(request):
	return render(request, 'rentals/delete_js.html')



def Convert(string): 
    li = list(string.split("[")) 
    return li 


