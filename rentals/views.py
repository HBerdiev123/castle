from django.shortcuts import render

# Create your views here.

def rent(request):
	return render(request, 'profile/property_detail1.html', {})

def rent_list(request):
	return render(request, 'listing/listing4.html', {})	
