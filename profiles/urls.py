from django.urls import path 
from . import views

app_name='profile'
urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('', views.profile, name='profile'),
	path('edit/', views.edit, name='edit'),
	path('favorites/', views.list_favorites, name='favorites'),
	path('add_fav/', views.add_to_favorities, name='add_fav'),
]