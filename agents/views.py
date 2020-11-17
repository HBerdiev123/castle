from django.shortcuts import render
from .models import Team
# Create your views here.

def list(request):
	agents = Team.objects.filter(is_active=True)
	return render(request, 'agent/agent_list.html', {"agents":agents})

def detail(request, id):
	agent  = Team.objects.get(id=id).filter(is_active=True)
	return render(request, 'agent/agent_profile.html', {'agent':agent})	