from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.http import HttpResponse

# Create your views here.
@login_required
def profile(request):
	return render(request, 'profile/profile.html', {})

def register(request):
	if request.method == 'POST':
		form  = UserRegistrationForm(request.POST)
		print('validating the user')
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			print('saving user into database')
			new_user.save()
			return render(request, 'profile/profile.html', {'new_user':new_user})
		else:
			# print(form.errors)
			pass	
	else:
		form  = UserRegistrationForm()
	return render(request, 'registration/register.html', {'user_form':form})	