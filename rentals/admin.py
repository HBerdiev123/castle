from django.contrib import admin
from .models import Picture, Feature, PropertyCategory, Properties, Message

# Register your models here.



 #    title			=models.CharField(max_length=255)
	# house_number	=models.CharField(max_length=255, blank=True)
	# street          =models.CharField(max_length=255)
	# city			=models.CharField(max_length=255, blank=True)
	# region			=models.CharField(max_length=255, blank=True)
	# postal_Code		=models.CharField(max_length=255, blank=True)
	# country			=models.CharField(max_length=255)
	# latitude        =models.DecimalField(max_digits=22, decimal_places=16)
	# longitude       =models.DecimalField(max_digits=22, decimal_places=16)
	# description     =RichTextField()
	# created 


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	list_filter = ('title', 'created')
	search_fields = ('title', 'created', 'description')
	# raw_id_fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('title', 'created')

@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	list_filter = ('title', 'created')
	search_fields = ('title', 'created', 'description')
	# raw_id_fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('title', 'created')

# class PropertyTabularInline(admin.TabularInline):
# 	model=Property
	

# class AddressAdmin(admin.ModelAdmin):
# 	inline=[PropertyTabularInline]
	
# admin.site.register(Address, AddressAdmin)
# admin.site.register(Property)


# class PropertyInline(admin.StackedInline):
# 	model = Properties


# class AddressAdmin(admin.ModelAdmin):
#     inlines = [
#         PropertyInline,
#     ]
# admin.site.register(Address, AddressAdmin)

from django.forms import CheckboxSelectMultiple
from django.db import models

admin.site.register(Message)

class PropertyAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
		}
  
admin.site.register(Properties, PropertyAdmin)
# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
# 	list_display = ('title',  'created')
# 	list_filter = ('title',  'created')
# 	search_fields = ('title', 'location', 'created', 'description')
# 	# raw_id_fields = ('title',)
# 	date_hierarchy = 'created'
# 	ordering = ('title', 'created')


# @admin.register(Property)

# class PropertyAdmin(admin.ModelAdmin):
# 	list_display = ('created')
# 	list_filter = ( 'created')
# 	search_fields = ('title', 'created', 'description')
# 	# raw_id_fields = ('title',)
# 	date_hierarchy = 'created'
# 	ordering = ('created')

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
	list_display = ('title', 'created')
	list_filter = ('title', 'created')
	search_fields = ('title', 'created', 'description')
	# raw_id_fields = ('title',)
	date_hierarchy = 'created'
	ordering = ('title', 'created')