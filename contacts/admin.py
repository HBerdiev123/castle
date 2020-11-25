from django.contrib import admin
from .models import Emails, EmailToAgent, ReplyLetter
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.

def email_detail(obj):
	url = reverse('profile:admin_email_detail', args=[obj.id])
	return mark_safe(f'<a href="{url}">View</a>')
	
# Register your models here.

admin.site.register(Emails)
admin.site.register(ReplyLetter)

# class AgentToEmailAdmin(admin.ModelAdmin):
# 	def save_model(self, request, obj, form, change):
# 		obj.agent = form.agent
# 		# def save_model(self, request, obj, form, change):
# 		# if not obj.user.id:
# 		# obj.user = request.user
# 		obj.save()

@admin.register(EmailToAgent)
class EmailToAgent(admin.ModelAdmin):
	list_display = [
		'sender',
		'phone_number',
		'agent',
		email_detail,
	]
# admin.site.register(EmailToAgent)