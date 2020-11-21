from django.contrib import admin
from .models import Profile
from .models import Team
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'mobile']


# @admin.register(MyFavorites)
# class MyFavoritesAdmin(admin.ModelAdmin):
# 	list_display = ['user', 'appartment']	


class TeamAdmin(admin.ModelAdmin):
	search_fields = ('user',)
	list_display = ('user', 'mobile', 'occupation')
	list_filter  = ('created_at',)
	search_fields = ('usernam', 'about')
	date_hierarchy = 'created_at'
	exclude = ('my_favorities',)
	ordering       = ['created_at']

admin.site.register(Team, TeamAdmin)