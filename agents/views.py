from django.shortcuts    import render
from profiles.models     import Team
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from contacts.forms   import AgentForm, ContactForm


# Create your views here.

# def list(request):
# 	agents  = get_user_model().objects.filter(is_active=True, is_staff=True).exclude(is_superuser=True)
# 	# agents = Team.objects.all()
# 	return render(request, 'agent/agent_list.html', {"agents":agents})

# def detail(request, id):
# 	agent  = get_user_model.objects.get(id=id).filter(is_active=True)
# 	if request.method=='POST':
#     	form = ContactForm(request.POST)
#     	if form.is_valid():
#     		data = form.cleanded_data
#     		data.save()
#     else:
#     	form = ContactForm()
# 	return render(request, 'agent/agent_profile.html', {'agent':agent, 'form':form, 'free':'free'})	

