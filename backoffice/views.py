from django.shortcuts import render
from rentals.models import Properties, Feature, Picture, PropertyCategory, Message, ReplyMessage
from rentals.forms import SearchForm, MessageForm
from .forms import SearchMessage
from .forms import PropertyForm, FeatureForm, PropertyCategoryForm, PropertyPicture, ReplyMessageForm
from django.contrib.postgres.search import TrigramSimilarity
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound                                               
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from contacts.forms import SocialContactForm, ContactNumberForm, TwilloContactForm
from contacts.models import SocialContact, ContactNumber, TwilloContact
from django.db.models.functions import Greatest

from django.contrib.auth.decorators import permission_required, login_required

# import smtplib
from django.core import mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

@login_required
def index(request):
	form = SearchForm()
	properties=Properties.objects.all()
	property_category=PropertyCategory.objects.all().distinct()
	property_purpose=Properties.PROPERTY_PURPOSE
    
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
	# results = []
	# if request.method=="GET":
	# 	form = SearchForm(request.GET)
	# 	if form.is_valid():
	# 		query 		  =form.cleaned_data['query']
	# 		min_bed       =form.cleaned_data['min_bed']
	# 		min_bath	  =form.cleaned_data['min_bath']
	# 		min_area	  =form.cleaned_data['min_area']
	# 		max_area	  =form.cleaned_data['max_area']
	# 		available_from=form.cleaned_data['available_from']
	# 		location      =form.cleaned_data['location']
	# 		category      =form.cleaned_data['category']
	# 		min_price 	  =form.cleaned_data['min_price']
	# 		max_price     =form.cleaned_data['max_price']
	# 		purpose		  =form.cleaned_data['purpose']
	# 		results 	= Properties.objects.active_status().all()

	# 		if query:
	# 			results=results.annotate(similarity=TrigramSimilarity("title", query),
	# 				).filter(similarity__gt=0.1).order_by('-similarity')

	# 		if location:
	# 			result=results.filter(address=location)

	# 		if min_bed:
	# 			results=results.filter(bedroom__gte=min_bed)

	# 		if category:
	# 			results=results.filter(category=category)

	# 		if min_bath:
	# 			results=results.filter(bathroom__gte=min_bath)

	# 		if min_area:
	# 			results=results.filter(size__gte=min_area)

	# 		if max_area:
	# 			results=results.filter(size__lte=max_area)

	# 		if available_from:
	# 			results=results.filter(available_from__gte=available_from)

	# 		if min_price:
	# 			results=results.filter(price__gte=min_price)

	# 		if max_price:
	# 			results=results.filter(price__lte=max_price)

	# 		if purpose:
	# 			results=results.filter(purpose=purpose)

	# 		if not query and not min_bed and not purpose and not category and not min_bath and not min_area and not max_area and not available_from and not location and not min_price and not max_price:
	# 			results 	= Properties.objects.active_status().all()
	# else:
	# 	form = SearchForm()
	properties=Properties.objects.active_status()
	results=Properties.objects.active_status().all()
	
	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"category":category,
		'all_properties': results,
		'property':properties,
		"properties":properties,
		"purpose":purpose,
		'property_category':property_category,
		'property_purpose':property_purpose,

	}


	return render(request, 'backoffice/index.html', context)



@login_required
def activeproperties(request):
	form = SearchForm()
	properties=Properties.objects.all()
	property_category=PropertyCategory.objects.all().distinct()
	property_purpose=Properties.PROPERTY_PURPOSE

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
	results=Properties.objects.active_status().all()
	
	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"category":category,
		'all_properties': results,
		'property':properties,
		"properties":properties,
		"purpose":purpose,
		'property_category':property_category,
		'property_purpose':property_purpose,

	}

	return render(request, 'backoffice/index.html', context)

@login_required
def propertyforsale(request):
	form = SearchForm()
	properties=Properties.objects.all().filter(purpose='1')
	property_category=PropertyCategory.objects.all().distinct()
	property_purpose=Properties.PROPERTY_PURPOSE
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
	results=Properties.objects.active_status().all()
	
	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"category":category,
		'all_properties': results,
		'property':properties,
		"properties":properties,
		"purpose":purpose,
		'property_category':property_category,
		'property_purpose':property_purpose,

	}

	return render(request, 'backoffice/index.html', context)



@login_required
def propertyforrent(request):
	form = SearchForm()
	properties=Properties.objects.all().filter(purpose='0')
	property_category=PropertyCategory.objects.all().distinct()
	property_purpose=Properties.PROPERTY_PURPOSE

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
	purpose=0
	results=Properties.objects.active_status().all()
	
	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"category":category,
		'all_properties': results,
		'property':properties,
		"properties":properties,
		"purpose":purpose,
		'property_category':property_category,
		'property_purpose':property_purpose,

	}

	return render(request, 'backoffice/index.html', context)


@login_required
def allproperty(request):
	all_property=Properties.objects.allproperties()
	page = request.GET.get('page', None)
	paginator = Paginator(all_property, 20)
	try:
		all_properties = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		all_properties = paginator.page(1)
	except EmptyPage:
		all_properties = paginator.page(paginator.num_pages)

	context={
	'properties':all_properties,

	}
	return render(request, 'backoffice/allproperty.html', context)


@login_required
def search_and_filter(request):
	form = SearchForm()
	properties=Properties.objects.all()
	property_category=PropertyCategory.objects.all().distinct()
	property_purpose=Properties.PROPERTY_PURPOSE
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
			purpose		  =form.cleaned_data['purpose']

			results 	= Properties.objects.active_status().all()

			if query:
				results=results.annotate(similarity=TrigramSimilarity("title", query),
					).filter(similarity__gt=0.1).order_by('-similarity')

			if location:
				result=results.filter(address=location)

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

			if not query and not min_bed and not purpose and not category and not min_bath and not min_area and not max_area and not available_from and not location and not min_price and not max_price:
				results 	= Properties.objects.active_status().all()
	else:
		form = SearchForm()
	# properties=Properties.objects.active_status()
	
	context={
		'form': form,
		'query': query, 
		'min_bed':min_bed,
		"min_bath":min_bath,
		"min_area":min_area,
		"max_area":max_area,
		"category":category,
		"purpose":purpose,
		'location':location,
		'available_from':available_from,
		'all_properties': results,
		'property':properties,
		"properties":results,
		 'min_price':min_price,
		'max_price':max_price,
		
		'property_category':property_category,
		'property_purpose':property_purpose,

	}

	# return render(request, 'backoffice/snippets/list_table.html', context)

	return render(request, 'backoffice/index.html', context)



from .forms import PropertyForm
from django.urls import reverse_lazy

from .forms import PictureForm
from django.http import JsonResponse
from django.views import View

# class BasicUploadView(View):
# 	def get(self, request):
# 		photos_list = Picture.objects.all()
# 		return render(self.request, 'backoffice/snippets/test.html', {'photos': photos_list})

# 	def post(self, request):
# 		form = PictureForm(self.request.POST, self.request.FILES)
# 		if form.is_valid():
# 			photo = form.save()
# 			data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
# 		else:
# 			data = {'is_valid': False}
# 		return JsonResponse(data)

@login_required
def new_property(request):
	id=None
	properties=Properties()
	property_form=PropertyForm(instance=properties)
	property_category=PropertyCategory.objects.all().distinct()
	PictureFormSet=inlineformset_factory(Properties, Picture, form=PictureForm, can_delete=True, min_num=1, validate_min=True, extra=0)	# PropertyFormSet = PropertyFormSets()
	formset=PictureFormSet(instance=properties)
	if request.method == "POST":
		property_form = PropertyForm(request.POST, request.FILES)
		formset=PictureFormSet(request.POST, request.FILES)
		if formset.is_valid()  and  property_form.is_valid():
			created_property=property_form.save(commit=False)
			formset=PictureFormSet(request.POST or None, request.FILES or None, instance=created_property)
			files=request.FILES

			if formset.is_valid():
				created_property.save()
				property_form.save_m2m()
				property_id=created_property.id
				title=property_form.cleaned_data['title']
				for key in files:
					Picture.objects.create(title=title, properties=Properties.objects.get(id=property_id), picture=files[key])
				
				# for key in files:
				# 	Picture.objects.create(title=title, properties=Properties.objects.get(id=property_id), picture=key)
				return render(request, 'backoffice/index.html')
			# else:
			# 	property_form = PropertyForm(instance=properties)
			# 	formset=formset=PictureFormSet()
	else:
		property_form = PropertyForm(instance=properties)
		formset=PictureFormSet(instance=properties)
	context={
		'property_form': property_form, 
		'formset':formset,
		'id':id,
		'property_category':property_category,
		}

	return render(request, 'backoffice/new_property.html', context)


@login_required
def manage_properties(request, id=None):
	# if id:
	# 	properties =get_object_or_404(Properties, pk=id)
	# 	images=Picture.objects.filter(properties=id) 
	# else:
	# 	properties=PropertyForm()
		# images=PictureFormSet(instance=images)
	id=id
	images=Picture.objects.filter(properties=id) 
	
	properties =get_object_or_404(Properties, pk=id)
	selected_category=properties.category.id
	latitude=properties.latitude
	longitude=properties.longitude
	
	property_category=PropertyCategory.objects.all().distinct().exclude(id=selected_category)
	PictureFormSet=inlineformset_factory(Properties, Picture, form=PictureForm, can_delete=True, min_num=1, validate_min=True, extra=0)	# PropertyFormSet = PropertyFormSets()
	formset=PictureFormSet(instance=properties)
	
	if request.method == "POST":
		property_form = PropertyForm(request.POST, request.FILES)
		formset=PictureFormSet(request.POST, request.FILES)
	

		property_form = PropertyForm(request.POST, request.FILES, instance=properties)
		formset=PictureFormSet(request.POST or None, request.FILES or None)
		if property_form.is_valid():
			created_property=property_form.save(commit=False)
			# created_property.save_m2m()
			formset=PictureFormSet(request.POST or None, request.FILES or None, instance=created_property)
			files=request.FILES.getlist('picture_set-0-picture')
			if formset.is_valid():
				created_property.save()
				property_form.save_m2m()
				
				# formset.save()
				property_id=id
				title=property_form.cleaned_data['title']
				for key in files:
					# file_instance=Picture(properties=property_id, picture=key)
					# file_instance.save()
					
					Picture.objects.create(title=title, properties=Properties.objects.get(id=property_id), picture=key)
				return render(request, 'backoffice/index.html')
			else:
				formset=PictureFormSet(request.POST or None, request.FILES or None, instance=properties)

	else:
		property_form = PropertyForm(instance=properties)
		formset=PictureFormSet()
	
	context={
		'property_form': property_form, 
		'formset':formset,
		'images':images,
		'id':id,
		'property_category':property_category,
		'selected_category':selected_category,
		'latitude':latitude,
		'longitude':longitude,

		}

	return render(request, 'backoffice/new_property.html', context)



@login_required
def uploadpicture(request):
	if request.method == "POST":
		if request.is_ajax():
			form = PictureForm(data=request.POST, files=request.FILES)
			data=request.POST
			file=request.FILES
			id=data.get("id")
			properties=Properties.objects.get(id=id)
			image=file.get('id_picture')
			saveimage=Picture.objects.create(properties=properties, picture=image)
			if saveimage:
				data = {'is_valid': True}
			else:
				data = {'is_valid': False}
			return JsonResponse(data)

		# if form.is_valid():
		# 	image = form.save()
		# 	print('??????????????')

		# 	data = {'is_valid': True, 'name': picture.image.name, 'url': picture.image.url}
		# else:
			# print(' invalid ??????????????')
			# data = {'is_valid': False}
		
	# return None






# @login_required
# def uploadpicture(self, request):
# 	print('??????????????')
	
# 	form = PictureForm(self.request.POST, self.request.FILES)
# 	print('??????????????')
# 	print(form)
# 	if form.is_valid():
# 		image = form.save()
# 		print('saved??????????????')
# 		data = {'is_valid': True, 'name': picture.image.name, 'url': picture.image.url}
# 	else:
# 		print(' invalid ??????????????')
# 		data = {'is_valid': False}
# 	return JsonResponse(data)




@login_required


# from .forms import PictureForm
# @login_required
# def manage_properties(request, id=None):
# 	# if id:
# 	# 	properties =get_object_or_404(Properties, pk=id)
# 	# 	images=Picture.objects.filter(properties=id) 
# 	# else:
# 	# 	properties=PropertyForm()
# 		# images=PictureFormSet(instance=images)
# 	images=Picture.objects.filter(properties=id) 
# 	properties =get_object_or_404(Properties, pk=id)
# 	formset=PictureForm(instance=properties)
	
# 	if request.method == "POST":
# 		property_form = PropertyForm(request.POST, request.FILES, instance=properties)
# 		formset=PictureForm(request.POST or None, request.FILES or None)
# 		if formset.is_valid()  and  property_form.is_valid():
# 			created_property=property_form.save(commit=False)
# 			formset=PictureForm(request.POST or None, request.FILES.getlist('picture_set-0-picture') or None, instance=created_property)
# 			# files=request.FILES.getlist('picture_set-0-picture')
# 			if formset.is_valid():
# 				created_property.save()
# 				formset.save()

# 				# property_id=id
# 				# title=property_form.cleaned_data['title']
# 				# for key in files:
# 				# 	file_instance=Picture(properties=property_id, picture=key)
# 				# 	file_instance.save()
# 					# print(';;;;;;;;;;;;;;;;;;;')
# 					# print(key)
# 					# Picture.objects.update(title=title, properties=Properties.objects.filter(id=property_id), picture=key)
# 				return render(request, 'backoffice/index.html')
# 	else:
# 		property_form = PropertyForm(instance=properties)
# 		formset=PictureForm(instance=properties)
# 		print('this is not pos request')
	
# 	context={
# 		'property_form': property_form, 
# 		'formset':formset,
# 		'images':images,
# 		}

# 	return render(request, 'backoffice/new_property.html', context)


		# address_form=AddressForm(instance=address)

		# formset = PropertyInlineFormSet(instance=address)
	# return render(request, 'backoffice/manage_properties.html', {'formset': formset, 'address_form':address_form,})

@login_required
def propertyDeleteView(request):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		properties =get_object_or_404(Properties, pk=get_data['pk'])
		get_linked_pictures=Picture.objects.filter(properties=get_data['pk'])
		for i in get_linked_pictures:
			i.picture.delete()
		if properties.delete() and get_linked_pictures.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")
		
@login_required
def change_status(request):
	if request.POST:
		get_request=request.POST
		status=get_request.get('status', False)
		get_id=get_request.get('pk', False)
		# get_property=get_object_or_404(Properties, id=get_id)
		# print(get_property)
		if status=='inactive':
			Properties.objects.allproperties().filter(id=get_id).update(status='0')
			data = {'status':'status is set to inactive'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			Properties.objects.allproperties().filter(id=get_id).update(status='1')
			data = {'status':'status is set to active'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		
	else:
		data = {'message':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
def send_property(request):

	if request.method == "POST":
		
		query=request.POST.get('query', '')
		category=request.POST.get('category', '')
		purpose=request.POST.get('purpose', '')
		available_from=request.POST.get('available_from', '')
		min_bed=request.POST.get('min_bed', '')
		min_bath=request.POST.get('min_bath', '')
		min_area=request.POST.get('min_area', '')
		max_area=request.POST.get('max_area', '')
		min_price=request.POST.get('min_price', '')
		max_price=request.POST.get('max_price', '')
		recipient_phone_number=request.POST.get('recipient_phone_number', '')
		recipient_email=request.POST.get('recipient_email', '')
		context={
		
		}

		if recipient_email:
			html_message = render_to_string('backoffice/snippets/email_template.html', context)
			send_mail('Subject', html_message, 'cloud.berdiyev@gmail.com',  [recipient_email], html_message=html_message)
		# replyForm.save()
		# data = {'status':'sent'}
		# return HttpResponse(json.dumps(data), content_type="application/json")



		new_url='http://127.0.0.1:8000/rentals/search/?query=%s&location=&category=%s&purpose=%s&available_from=%s&min_bed=%s&min_bath=%s&min_area=%s&max_area=%s&min_price=%s&max_price=%s' % (query, category, purpose, available_from, min_bed, min_bath,  min_area, max_area, min_price, max_price)

		# Your Account Sid and Auth Token from twilio.com/console
		# and set the environment variables. See http://twil.io/secure
		twilloaccount=TwilloContact.objects.all().last()
		account='ACb68fa66b2e3a3cd32d25c37542db4f36'
		token='010d58583d65ff34a2acd9584b01240e'
		
		# account = twilloaccount.twillo_account
		# token = twilloaccount.twillo_token
		print('twillo details')
		print(account)
		print(token)
		client = Client(account, token)

		
		try:
		  message = client.messages.create(from_='+19166195461', to='+4915775140214', body=new_url)

		  # message = client.messages.create(from_='+19166195461', to='+491784047362', body=new_url, url=new_url)
		  print(message.sid)


		except TwilioRestException as e:
			data = {'status':e}
			return HttpResponse(json.dumps(data), content_type="application/json")
# 491784047362
		# message = client.messages.create(body='testing', from_='+19166195461', to='+4915775140214')
		# if message:
		# 	print('it works')
	else:
		data = {'status':'Failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")


# class ManageFeature(generic.DetailView):
# 	model=Feature
# 	template_name='backoffice/manage_features.html'

# 	def get_queryset(self):
# 		return get_object_or_404(Feature, pk=self.kwargs['pk'])


@login_required
def features(request):
	all_features=Feature.objects.all()
	context={
		'feature_form':all_features,
	}
	return render(request, 'backoffice/all_features.html', context)




@login_required
def create_feature(request):
	context={}
	if request.method == "POST":
		featuries=FeatureForm(request.POST)
		if featuries.is_valid():
			featuries.save()
			return redirect('backoffice:features')
			
	else:
		featuries =FeatureForm()
		
	context={
		'feature_form': featuries, 
		}
	return render(request, 'backoffice/manage_features.html', context)

@login_required
def manage_feature(request, id=None):
	context={}
	featuries =get_object_or_404(Feature, pk=id)
	if request.method == "POST":
		featuries=FeatureForm(request.POST or None, instance=featuries)
		if featuries.is_valid():
			featuries.save()
			return redirect('backoffice:features')
	else:
		featuries =FeatureForm(request.POST or None, instance=featuries)
		
	context={
		'feature_form': featuries, 
		}
	return render(request, 'backoffice/manage_features.html', context)


@login_required
def delete_feature(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		feature =get_object_or_404(Feature, pk=get_data['pk'])
		if feature.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")
	

@login_required
def property_category(request):
	property_categories=PropertyCategory.objects.all()
	context={
		'property_categories':property_categories,
	}
	return render(request, 'backoffice/all_property_categories.html', context)

@login_required
def create_property_category(request):
	context={}
	if request.method == "POST":
		property_categories=PropertyCategoryForm(request.POST)
		if property_categories.is_valid():
			property_categories.save()
			return redirect('backoffice:property_categories')
	else:
		property_categories =PropertyCategoryForm()
		
	context={
		'property_categories': property_categories, 
		}
	return render(request, 'backoffice/manage_property_category.html', context)


@login_required
def manage_property_category(request, id=None):
	context={}
	property_categories =get_object_or_404(PropertyCategory, pk=id)
	if request.method == "POST":
		property_categories=PropertyCategoryForm(request.POST or None, instance=property_categories)
		if property_categories.is_valid():
			property_categories.save()
			return redirect('backoffice:property_categories')
	else:
		property_categories =PropertyCategoryForm(request.POST or None, instance=property_categories)
		
	context={
		'property_categories': property_categories, 
		}
	return render(request, 'backoffice/manage_property_category.html', context)


@login_required
def delete_property_category(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		property_categories =get_object_or_404(PropertyCategory, pk=get_data['pk'])
		if property_categories.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")
	




@login_required
def property_picture(request):
	property_pictures=Picture.objects.all()
	context={
		'property_pictures':property_pictures,
	}
	return render(request, 'backoffice/all_pictures.html', context)


@login_required
def create_property_picture(request):
	context={}
	if request.method == "POST":
		property_pictures=PropertyPicture(request.POST, request.FILES)
		files=request.FILES.getlist('picture')
		print(files)
		print(property_pictures)
		if property_pictures.is_valid():
			for f in files:
				file_instance=Picture(picture=f)
				file_instance.save()
			return redirect('backoffice:property_pictures')
	else:
		property_pictures =PropertyPicture()
		
	context={
		'property_pictures': property_pictures, 
		}
	return render(request, 'backoffice/manage_property_pictures.html', context)

@login_required
class BasicUploadView(View):
    def get(self, request):
        photos_list = Picture.objects.all()
        return render(self.request, 'backoffice/manage_property_pictures.html', {'property_pictures': photos_list})

    def post(self, request):
        form = PropertyPicture(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': picture.file.name, 'url': picture.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

@login_required
def manage_property_picture(request, id=None):
	property_pictures =get_object_or_404(Picture, pk=id)
	if request.method == "POST":
		property_pictures=PropertyPicture(request.POST)
		if property_pictures.is_valid():
			property_pictures.save()
			return redirect('backoffice:property_pictures')
	else:
		property_pictures =PropertyCategoryForm()
		
	context={
		'property_pictures': property_pictures, 
		}
	return render(request, 'backoffice/manage_property_pictures.html', context)


@login_required
def delete_property_picture(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		property_pictures =get_object_or_404(Picture, pk=get_data['pk'])
		# and property_pictures.picture.delete():
		if property_pictures.delete(): 
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")
	


@login_required
def search_message(request):
	search_message=SearchMessage()
	query=None
	phone_number=None
	start_date=None
	end_date=None
	status=None
	messages = []
	if request.method=="GET":
		search_message = SearchForm(request.GET)
		if search_message.is_valid():
			query        =request.GET.get('query')
			start_date   =request.GET.get('start_date')
			end_date     =request.GET.get('end_date')
			# full_name	 =search_message.cleaned_data['full_name']
			phone_number =request.GET.get('phone_number')
			# email        =search_message.cleaned_data['email']
			# message      =search_message.cleaned_data['message']
			# title        =search_message.cleaned_data['title']
			# reply_message=search_message.cleaned_data['reply_message']
			status       =request.GET.get('status')
			
			messages   	 = Message.objects.all()

			# if query:
			# 	messages=messages.annotate(similarity=Greatest(TrigramSimilarity("full_name", query), TrigramSimilarity("message", query), 
			# 		TrigramSimilarity("title", query), TrigramSimilarity("reply_message", query), TrigramSimilarity("email", query),
			# 		)).filter(similarity__gt=0.1).order_by('-similarity')
			if query:
				messages=messages.annotate(similarity=Greatest(TrigramSimilarity("full_name", query), TrigramSimilarity("message", query), 
					TrigramSimilarity("email", query),
					)).filter(similarity__gt=0.1).order_by('-similarity')

			if phone_number:
				messages=messages.filter(phone_number=phone_number)
			if start_date:
				messages=messages.filter(created__gte=start_date)
			if end_date:
				messages=messages.filter(created__lte=end_date)
			if status:
				messages=messages.filter(status=status)
			if not query and not status and phone_number:
				messages 	= Properties.objects.all()


	else:
		search_message=SearchForm()
	page = request.GET.get('page', None)
	paginator = Paginator(messages, 5)
	try:
		all_messages = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		all_messages = paginator.page(1)
	except EmptyPage:
		all_messages = paginator.page(paginator.num_pages)


	context={
	'query':query,
	'phone_number':phone_number,
	'status':status,
	'message_form':all_messages,
	}

	return render(request, 'backoffice/snippets/messages_list_table.html', context)





@login_required
def show_all_messages(request):
	messages=Message.objects.all()
	user=request.user.id
	title=None
	reply_message=None
	if request.method == "POST":
		title		   ='reply'
		reply_message =request.POST.get('reply_message') 
		message        =request.POST.get('message')
		save_reply=ReplyMessage(title=title, reply_message=reply_message)
		save_reply.save()
		save_reply.message.set([message])
		save_reply.user.set([user])
		if save_reply:
			change_message_status=Message.objects.filter(id=message).update(status="1")

		context={
			'title':title,
			'replay_message':reply_message,
		}
		html_message = render_to_string('backoffice/snippets/email_template.html', context)
		send_mail('Subject', html_message, 'cloud.berdiyev@gmail.com',  ['developercontact@yandex.ru'], html_message=html_message)
		# data = {'status':'sent'}
		# return HttpResponse(json.dumps(data), content_type="application/json")
		return render(request, 'backoffice/snippets/reply_message_snippet.html', {'replymessage':save_reply})
	else:
		replyForm =ReplyMessageForm()

	page = request.GET.get('page', None)
	paginator = Paginator(messages, 5)
	try:
		all_messages = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		all_messages = paginator.page(1)
	except EmptyPage:
		all_messages = paginator.page(paginator.num_pages)

	context={
	'reply_form':replyForm,
	'user':user,
	'message_form':all_messages,
	}

	return render(request, 'backoffice/all_messages.html', context)





@login_required
def not_replied_messages(request):
	messages=Message.objects.all().filter(status='0')
	user=request.user.id
	title=None
	reply_message=None
	if request.method == "POST":
		title		   ='reply'
		reply_message =request.POST.get('reply_message') 
		message        =request.POST.get('message')
		save_reply=ReplyMessage(title=title, reply_message=reply_message)
		save_reply.save()
		save_reply.message.set([message])
		save_reply.user.set([user])
		if save_reply:
			change_message_status=Message.objects.filter(id=message).update(status="1")

		context={
			'title':title,
			'replay_message':reply_message,
		}
		html_message = render_to_string('backoffice/snippets/email_template.html', context)
		send_mail('Subject', html_message, 'cloud.berdiyev@gmail.com',  ['developercontact@yandex.ru'], html_message=html_message)
		# data = {'status':'sent'}
		# return HttpResponse(json.dumps(data), content_type="application/json")
		return render(request, 'backoffice/snippets/reply_message_snippet.html', {'replymessage':save_reply})
		
	else:
		replyForm =ReplyMessageForm()
		
	page = request.GET.get('page', None)
	paginator = Paginator(messages, 5)
	try:
		all_messages = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer deliver the first page
		all_messages = paginator.page(1)
	except EmptyPage:
		all_messages = paginator.page(paginator.num_pages)


	context={
	'reply_form':replyForm,
	'user':user,
	'message_form':all_messages,
	}

	return render(request, 'backoffice/all_messages.html', context)


@login_required
def delete_message(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		message =get_object_or_404(Message, pk=get_data['pk'])
		if message.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")
	




@login_required
def create_social_contact(request):
	context={}
	if request.method == "POST":
		social_contact=SocialContactForm(request.POST)
		if social_contact.is_valid():
			social_contact.save()
			return redirect('backoffice:social_contact')
			
	else:
		social_contact =SocialContactForm()
		
	context={
		'social_contact_form': social_contact, 
		}
	return render(request, 'backoffice/manage_social_contact.html', context)

@login_required
def manage_social_contact(request, id=None):
	context={}
	social_contact =get_object_or_404(SocialContact, pk=id)
	if request.method == "POST":
		social_contact=SocialContactForm(request.POST or None, instance=social_contact)
		if social_contact.is_valid():
			social_contact.save()
			return redirect('backoffice:social_contact')
	else:
		social_contact =SocialContactForm(request.POST or None, instance=social_contact)
		
	context={
		'social_contact_form': social_contact, 
		}
	return render(request, 'backoffice/manage_social_contact.html', context)


@login_required
def delete_social_contact(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		social_contact =get_object_or_404(SocialContact, pk=get_data['pk'])
		if social_contact.delete():
			data = {'status':'deletSocialContacted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")

@login_required
def social_contact(request):
	social_contacts=SocialContact.objects.all()
	context={
		'social_contacts':social_contacts,
	}
	return render(request, 'backoffice/all_social_contacts.html', context)

@login_required
def create_contact_number(request):
	context={}
	if request.method == "POST":
		contact_number=ContactNumberForm(request.POST)
		if contact_number.is_valid():
			contact_number.save()
			return redirect('backoffice:contact_number')
			
	else:
		contact_number =ContactNumberForm()
		
	context={
		'contact_number_form': contact_number, 
		}
	return render(request, 'backoffice/manage_contact_number.html', context)

@login_required
def manage_contact_number(request, id=None):
	context={}
	contact_number =get_object_or_404(ContactNumber, pk=id)
	if request.method == "POST":
		contact_number=ContactNumberForm(request.POST or None, instance=contact_number)
		if contact_number.is_valid():
			contact_number.save()
			return redirect('backoffice:contact_number')
	else:
		contact_number =ContactNumberForm(request.POST or None, instance=contact_number)
		
	context={
		'contact_number_form': contact_number, 
		}
	return render(request, 'backoffice/manage_contact_number.html', context)


@login_required
def delete_contact_number(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		contact_number =get_object_or_404(ContactNumber, pk=get_data['pk'])
		if contact_number.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
def contact_number(request):
	contact_numbers=ContactNumber.objects.all()
	context={
		'contact_numbers':contact_numbers,
	}
	return render(request, 'backoffice/all_contact_numbers.html', context)


@login_required
def create_twillo(request):
	context={}
	if request.method == "POST":
		twillo_form=TwilloContactForm(request.POST)
		if twillo_form.is_valid():
			twillo_form.save()
			return redirect('backoffice:twillo')
			
	else:
		twillo_form =TwilloContactForm()
		
	context={
		'twillo_form': twillo_form, 
		}
	return render(request, 'backoffice/manage_twillo.html', context)

@login_required
def manage_twillo(request, id=None):
	context={}
	twillo_form =get_object_or_404(TwilloContact, pk=id)
	if request.method == "POST":
		twillo_form=TwilloContactForm(request.POST or None, instance=twillo_form)
		if twillo_form.is_valid():
			twillo_form.save()
			return redirect('backoffice:twillo')
	else:
		twillo_form =TwilloContactForm(request.POST or None, instance=twillo_form)
		
	context={
		'twillo_form': twillo_form, 
		}
	return render(request, 'backoffice/manage_twillo.html', context)


@login_required
def delete_twillo(request, id=None):
	context ={}
	get_data=request.POST
	if request.method == "POST":
		twillo_form =get_object_or_404(TwilloContact, pk=get_data['pk'])
		if twillo_form.delete():
			data = {'status':'deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
		else:
			data = {'status':'not deleted'}
			return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data = {'status':'failed'}
		return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
def twillo(request):
	twillo_form=TwilloContact.objects.all()
	context={
		'twillo_form':twillo_form,
	}
	return render(request, 'backoffice/all_twillo.html', context)

