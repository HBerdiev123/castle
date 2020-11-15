from django.shortcuts import render
from .models import FAQ, Partners
# Create your views here.


def faq(request):
	# faq = FAQ.objects.filter(is_active=True)
	# return render(request, 'faq/faq.html', {'faq':faq})
