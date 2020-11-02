from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.rent, name='rent-detail'),
	url(r'^list$', views.rent_list, name='rent-list'),
]


