from django.contrib import admin
from .models import Team

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email_address', 'phone', 'is_active','occupation')
	list_filter  = ('created_at', 'is_active')
	search_fields = ('full_name', 'about_agent')
	date_hierarchy = 'created_at'
	ordering       = ['created_at']

admin.site.register(Team, TeamAdmin)