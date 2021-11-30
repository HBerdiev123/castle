from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http      import HttpResponse, HttpResponseRedirect
from additions.models import FAQ
from rentals.models   import Properties
from profiles.models  import Team 
from contacts.models  import Emails
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.views.decorators.vary  import vary_on_cookie
# from django.templates import RequestContext

@vary_on_cookie
@cache_page(60)
def home(request):
	hauses     = Properties.objects.all()[9:]
	print(hauses)
	teams    = User.objects.filter(is_active=True, is_staff=True)[3:] 
	featured = Properties.objects.filter(featured=True)[10:]
	
	return render(request, 'home/index.html',{
		'hauses':hauses,
		'teams':teams,
		'featured':featured})

@vary_on_cookie
@cache_page(3600)
def contacts(request):
	return render(request, 'contacts/contact.html',{})

@vary_on_cookie
@cache_page(3600)
def faq(request):
	faq = FAQ.objects.filter(is_active=True)
	# faq = FAQ.objects.all()
	return render(request, 'faq/faq.html', {'faq':faq})


def error_404(request):
	return render(request, 'errors/404.html')

def handler404(request, exception):
	return render(request, '404.html', {})

def handler500(request, *args, **kwargs):
	return render(request, '500.html', {})


def send_mail(request):
	subject = request.POST.get('subject','')
	message = request.POST.get('message', '')
	from_email= request.POST.get("from_email","")
	if subject and message and from_email:
		try:
			print('email has been sent successfully')
			send_mail(subject, message, from_email, ['admin@example.com'])
		except:
			return HttpResponse('Invalid header found.')
		return HttpResponseRedirect('/contact/thanks/')
	else:
		return HttpResponse('Make sure all fields are entered and valid.')	

			