from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
	return render(request, 'home/index.html',{})

def contacts(request):
	return render(request, 'contacts/contact.html',{})

def faq(request):
	return render(request, 'faq/faq.html')

def error_404(request):
	return render(request, 'errors/404.html')

def faq(request):
	return render(request,'faq/faq.html')



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