from django.conf.urls import url 
from . import views
from django.urls import path

app_name = 'news'
urlpatterns = [
	url(r'^$', views.list, name='list'),
	path('detail/<slug:slug>/', views.detail, name='detail'),
	path('tag/<slug:tag_slug>/', views.list, name='post_list_by_tag'), 
	path('cat/<slug:cat_slug>/', views.list, name='list_post_by_category'), 
	path('search/', views.post_search, name='search'),
]