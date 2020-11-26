from django.conf.urls import url
from . import views

# urlpatterns = [

# 	url(r'^$', views.rent, name='rent-detail'),
# 	url(r'^list$', views.rent_list, name='rent-list'),
# ]

from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import load_coordinates, rent_detail, property_search, getbyid_property

app_name = 'rentals'
urlpatterns = [

	url(r'^$', views.rent, name='rent-detail'),
	url(r'^list$', views.rent_list, name='rent-list'),
    # url(r'^(?P<id>[\w-]+)/$', rent_detail, name='detail'),
    path('<int:id>/', rent_detail, name='detail'),
    path('search/', property_search, name='property_search'),
    path('getbyid_property/', getbyid_property, name='getbyid_property'),
    # path('ajax_message_submit/', ajax_message_submit, name='ajax_message_submit'),
	path('load_coordinates/', load_coordinates, name='ajax_load_coordinates'),  # <-- this one here

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


