from django.urls import path
from . import views

app_name = 'additions'

urlpatterns   = [
   path('', views.faq, name='faq'),
]