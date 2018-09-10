"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
# tutorial said to replace all the contents here with below
# commented out incase we need the previous code --> gladys
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from catalog import views


urlpatterns = [
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private),
    url(r'index/', views.index),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    url(r'^advertisement/$', views.advertisement_list),
    url(r'^advertisement/(?P<pk>[0-9]+)/$', views.advertisement_detail),
    url(r'^userprofile/$', views.user_profile_list),
    url(r'^userprofile/(?P<pk>[0-9]+)/$', views.user_profile_detail),
    url(r'^userreview/$', views.user_review_list),
    url(r'^userreview/(?P<pk>[0-9]+)/$', views.user_review_detail),
]
