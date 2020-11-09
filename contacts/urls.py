from django.conf.urls import url 
from . import views
from django.urls import path

app_name = 'contacts'
urlpatterns =[
	path('', views.contact, name='contact'),
]