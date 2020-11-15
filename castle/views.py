from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from additions.models  import FAQ
# from django.templates import RequestContext


def home(request):
	return render(request, 'home/index.html',{})

def contacts(request):
	return render(request, 'contacts/contact.html',{})

def faq(request):
	faq = FAQ.objects.filter(is_active=True)
	# faq = FAQ.objects.all()
	return render(request, 'faq/faq.html', {'faq':faq})

def error_404(request):
	return render(request, 'errors/404.html')


def handler404(request, exception):
	# response = render_to_response('404.html', context_instance = RequestContext(request))
	# response.status_code=404
	# response = render(request, '404.html', {})
	# response.status_code = 404
	return render(request, '404.html', {})

def handler500(request, *args, **kwargs):
	# response = render_to_response('500.html', context_instance = RequestContext(request))
	# response.status_code=500
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