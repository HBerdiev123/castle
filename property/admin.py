from django.contrib import admin
from .models import Picture, Feature, PropertyCategory, Property, FeaturedProperties


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


class PropertyInline(admin.StackedInline):
	model = Property

class ImagesInline(admin.StackedInline):
	model = Picture
	extra = 6


from django.forms import CheckboxSelectMultiple
from django.db import models

class PropertyAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},
		}
	inlines = [ImagesInline]
	# exclude = ('user',)
	readonly_fields = ('user',)

	def save_model(self, request, obj, form, change):
		# if not obj.user.id:
		obj.user = request.user
		obj.save()	
  
admin.site.register(Property, PropertyAdmin)



@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	list_filter = ('title', 'created_at')
	search_fields = ('title', 'created_at', 'description')
	# raw_id_fields = ('title',)
	date_hierarchy = 'created_at'
	ordering = ('title', 'created_at')


@admin.register(FeaturedProperties)
class FeaturedPropertyAdmin(admin.ModelAdmin):
	list_display  = ('prop', 'is_active', 'created_at')
	list_filter   = ('is_active', 'created_at')	
	date_hierarchy='created_at'
	ordering      = ('updated_at', 'created_at')