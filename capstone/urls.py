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
    path('admin/', admin.site.urls),
    url(r'^advertisement/$', views.advertisement_list),
    url(r'^advertisement/(?P<pk>[0-9]+)/$', views.advertisement_detail),
]

'''
url(r'^userProfile/$', views.user_profile_list),
url(r'^userProfile/(?P<pk>[0-9]+)/$', views.user_profile_detail),
url(r'^userReview/$', views.user_review_list),
url(r'^userReview/(?P<pk>[0-9]+)/$', views.user_review_detail),
url(r'^accomReview/$', views.accommodation_review_list),
url(r'^accomReview/(?P<pk>[0-9]+)/$', views.accommodation_review_detail),
url(r'^amenities/$', views.amenities_list),
url(r'^amenities/(?P<pk>[0-9]+)/$', views.amenities_detail),
url(r'^propertyImage/$', views.property_image_list),
url(r'^propertyImage/(?P<pk>[0-9]+)/$', views.property_image_detail),
url(r'^event/$', views.event_list),
url(r'^event/(?P<pk>[0-9]+)/$', views.event_detail),
'''
