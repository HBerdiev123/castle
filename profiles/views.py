from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from .forms import LoginForm, UserEditForm, ProfileEditForm
from .models import Profile
# from .models import MyFavorites
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from property.models import Property 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required

# Create your views here.

def user_login(request):
	if request.method == "POST":
		form     = LoginForm(request.POST)
		if form.is_valid():
			cd   = form.cleaned_data
			user = authenticate(request, username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated Successfully')
				else:
					return HttpResponse('Disabled account')
		else:
			return HttpResponse('Invalid Login')
	else:
		form  = LoginForm()
	return render(request, 'profile/login.html', {'form':form})	


def register(request):
	if request.method == 'POST':
		form  = UserRegistrationForm(request.POST)
		print('validating the user')
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			print('saving user into database')
			new_user.save()
			Profile.objects.create(user=new_user)
			return render(request, 'profile/profile.html', {'new_user':new_user})
		else:
			# print(form.errors)
			pass	
	else:
		form  = UserRegistrationForm()
	return render(request, 'registration/register.html', {'user_form':form})



@login_required
def profile(request):
	profile = get_object_or_404(Profile, user=request.user)
	return render(request, 'profile/profile.html', {'profile':profile})

@login_required
# @require_POST
def edit(request):
	if request.method =="POST":
		user_form     = UserEditForm(instance=request.user, data=request.POST)
		profile_form  = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your profile updated successfully!')
		else:
			messages.error(request, 'Error updating your profile')	

		# image = Profile.objects.get(user=request.user).photo
		image = get_object_or_404(Profile, user=request.user).photo
			
	else:
		user_form     = UserEditForm(instance=request.user)
		profile_form  = ProfileEditForm(instance=request.user.profile)
		
		image = get_object_or_404(Profile, user=request.user).photo		
		
	return render(request, 'profile/edit.html',
					{'user':user_form,
					 'profile':profile_form, 'image':image})	 
	

@login_required
def list_favorites(request):
	# fav_list = MyFavorites.objects.filter(user=request.user)
	# properties = Property.objects.filter()
	profile =  Profile.objects.filter(user=request.user).first()
	return render(request, 'profile/list_favorites.html', {'profile':profile})



@ajax_required
@login_required
@require_POST
def add_to_favorities(request):
	app_id = request.POST.get('id')
	action = request.POST.get('action')
	if app_id and action:
		try:
			user = Profile.objects.get(user=request.user)
			if action =="like":
				user.my_favorities.add(app_id)
			else:
				user.my_favorities.remove(app_id)
			return JsonResponse({'status':'ok'})

		except:
			pass
	return JsonResponse({'status':'error'})		