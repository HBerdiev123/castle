"""castle URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rentals import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.home, name='home'),
    # url('^contacts$', views.contacts, name='contacts'),
    url(r'^rentals/', include('rentals.urls')),
    url(r'^news/',    include('news.urls', namespace="news")),
    url(r'^404$',views.error_404, name='error_404'),
    url(r'^faq/$', views.faq, name='faq'),
    # path('profile/', include('profiles.urls', namespace="profile")),
    path('account/',  include('account.urls', namespace='account')),
    path('profile/',  include('profiles.urls', namespace='profile')),
    path('accounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    url(r'$send/$', views.send_mail, name="send-mail" ),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)