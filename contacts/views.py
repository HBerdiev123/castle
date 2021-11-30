from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages



def contact(request):
	if request.method == 'POST':
		form = ContactForm(initial=request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'We have recived your message. We will responsece asp.')
		else:
			print(form.as_p)
			# print(form.cleaned_data)
			messages.error(request, 'Oops! Something went wrong')
			return render(request, 'contacts/contact.html',{'form':form})

	else:
		form = ContactForm()

	return render(request, 'contacts/contact.html',{'form':form})