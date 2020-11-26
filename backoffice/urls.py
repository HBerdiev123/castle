from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import index, search_and_filter, new_property, create_property_picture, create_property_category, create_feature, manage_properties, property_picture, manage_property_picture, delete_property_picture, property_category, manage_property_category, delete_property_category, manage_feature, propertyDeleteView, features, delete_feature 
# from .views import PictureList, PicturePropertyCreate


app_name = 'backoffice'
urlpatterns = [

  path('', index, name='index'),
  path('allproperty/', views.allproperty, name='allproperty'),
  path('activeproperty/', views.activeproperties, name='activeproperties'),
  path('propertyforsale/', views.propertyforsale, name='propertyforsale'),
  path('propertyforrent/', views.propertyforrent, name='propertyforrent'),

  path('search_and_filter/', search_and_filter, name='ajax_search_and_filter'),
  path('new_property/', new_property, name='new_property'),
  path('uploadpicture/', views.uploadpicture, name='uploadpicture'),
  path('manage_properties/<int:id>/', manage_properties, name='manage_properties'),
  path('delete/', propertyDeleteView, name='deleteproperty'),
  path('change_status/', views.change_status, name='changestatus'),
  path('features/', features, name='features'),
  path('create_feature/', create_feature, name='create_feature'),

  
  path('features/<int:id>/', manage_feature, name='managefeature'),
  path('delete_feature/', delete_feature, name='deletefeature'),
  path('property_categories/', property_category, name='property_categories'),
  path('create_property_category/', create_property_category, name='create_property_category'),
  # path('^fine-uploader/', include('django_fine_uploader.urls', namespace='django_fine_uploader')),

  
  path('property_categories/<int:id>/', manage_property_category, name='manage_property_category'),
  path('delete_property_category/', delete_property_category, name='delete_property_category'),

  path('property_pictures/', property_picture, name='property_pictures'),
  path('create_property_picture/', create_property_picture, name='create_property_picture'),

  # path('basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),

  path('property_pictures/<int:id>/', manage_property_picture, name='manage_property_picture'),
  path('delete_property_pictures/', delete_property_picture, name='delete_property_picture'),


  path('show_messages/', views.not_replied_messages, name='show_new_messages'),
  path('all_messages/', views.show_all_messages, name='all_messages'),
  path('search_message/', views.search_message, name='search_message'),
  
  path('delete_message/', views.delete_message, name='delete_message'),
  # url(r'ckeditor/', include('ckeditor_uploader.urls')),
  path('send_property_list/', views.send_property, name='send_property_list'),

  path('social_contact', views.social_contact, name='social_contact'),
  path('create_social_contact', views.create_social_contact, name='create_social_contact'),
  path('social_contact/<int:id>/', views.manage_social_contact, name='manage_social_contact'),
  path('delete_social_contact/', views.delete_social_contact, name='delete_social_contact'),
  

  path('contact_number', views.contact_number, name='contact_number'),
  path('create_contact_number', views.create_contact_number, name='create_contact_number'),
  path('contact_number/<int:id>/', views.manage_contact_number, name='manage_contact_number'),
  path('delete_contact_number/', views.delete_contact_number, name='delete_contact_number'),
  
  path('twillo', views.twillo, name='twillo'),
  path('create_twillo', views.create_twillo, name='create_twillo'),
  path('twillo/<int:id>/', views.manage_twillo, name='manage_twillo'),
  path('delete_twillo/', views.delete_twillo, name='delete_twillo'),
  




]
