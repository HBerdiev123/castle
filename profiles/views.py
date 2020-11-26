from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model 
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET

from common.decorators import ajax_required

from contacts.forms import AgentForm, ReplyForm
from .forms import LoginForm, UserEditForm, ProfileEditForm

# from .models import MyFavorites
from .models import Profile, Team
from contacts.models import EmailToAgent
from property.models import Property 
from profiles.models import Team


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
	try:
		profile = Profile.objects.get(user=request.user)
	except Profile.DoesNotExist:
		profile = Profile.objects.create(user=request.user)
		messages.info(request, 'You have not filled your account data!')

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

def is_ajax(request):
	return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def list_agents(request):
	agents  = get_user_model().objects.filter(is_active=True, is_staff=True).exclude(is_superuser=True)
	# agents = Team.objects.all()
	return render(request, 'agent/agent_list.html', {"agents":agents})

# @require_GET
def detail_agent(request, id):
	User  = get_user_model()
	agent = get_object_or_404(User, id=id, is_active=True)
	all_properties = Property.objects.filter(id=agent.id).order_by('-created')
	paginator  = Paginator(all_properties, per_page=10)
	page_num = int(request.GET.get('page', 1))
	if page_num>paginator.num_pages:
		raise Http404
	properties = paginator.page(page_num) 

	if is_ajax(request):
		return render(request, 'agent/_properties.html', {'properties':properties})	
	agent_id = agent.id
	if request.method=='POST':
		form = AgentForm(request.POST, initial={'agent':agent_id})
		print('post request recieved')
		if form.is_valid():
			form.save()
	else:
		
		form = AgentForm(initial={'agent':agent_id})		
	return render(request, 'agent/agent_profile.html', 
		{
		'agent':agent, 
		'properties':all_properties,
		'form':form
		})	

@staff_member_required
def admin_email_detail(request, email_id):
	email = get_object_or_404(EmailToAgent, id=email_id)
	agent = get_object_or_404(Team, id=email.agent.id)
	sender= email.agent.first_name + email.agent.last_name
	recipent = email.email
	if request.method =='POST':
		form = ReplyForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = ReplyForm(initial={'agent':agent.id, 'sender':sender, 'sender':recipent})	
	return render(request, 'admin/contacts/emailtoagent/detail.html', {'email':email, 'form':form})