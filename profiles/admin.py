from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'mobile']


# @admin.register(MyFavorites)
# class MyFavoritesAdmin(admin.ModelAdmin):
# 	list_display = ['user', 'appartment']	