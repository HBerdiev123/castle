from django.urls import path, include, re_path
from . import views

app_name = 'teams'
urlpatterns = [
	path('', views.list, name='list')
]