from django.contrib import admin
from .models import FAQ, Partners, Testimonal
# Register your models here.

class FAdmin(admin.ModelAdmin):
	list_display   = ('title', 'is_active', 'priority')
	list_filter    = ('is_active', 'created_at')
	search_fields  = ('title', 'body')
	date_hierarchy = 'created_at'
	ordering       = ['is_active']



admin.site.register(FAQ, FAdmin)

class PartnerAdmin(admin.ModelAdmin):
	list_display   = ('partner_name', 'priority', 'is_active')
	list_filter    = ('is_active',)
	search_fields  = ('partner_name',)
	date_hierarchy = 'created_at'
	ordering       = ['is_active']


admin.site.register(Partners, PartnerAdmin)


class TestimonialAdmin(admin.ModelAdmin):
	list_display  = ('full_name', 'company', 'is_active')
	list_filter   = ('is_active',)
	search_fields = ('full_name', 'company')
	date_hierarchy= 'created_at'
	ordering      = ['is_active']

admin.site.register(Testimonal, TestimonialAdmin)	