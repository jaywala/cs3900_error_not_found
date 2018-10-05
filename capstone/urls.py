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

'''
NOTE:
    - first refers to the part of the email before the @ sign
    - second refers to the part of the email after the @ sign
'''

urlpatterns = [

    # User Profile
    path('get/user/<slug:first>/<slug:second>/', views.user_profile_get),
    path('post/user/update/', views.user_profile_update),
    path('post/userLoggedIn/', views.is_loggedIn),

    #---------------- Poster Views ----------------#

    # Advertisement
    path('get/advertisement/<slug:first>/<slug:second>/', views.advertisement_get),
    path('post/advertisement/create/', views.advertisement_create),
    path('post/advertisement/update/', views.advertisement_update),
    path('post/advertisement/delete/', views.advertisement_delete),

    # Advertisement Review
    path('get/review/<slug:first>/<slug:second>/<slug:ad_id>/', views.review_get),
    path('post/review/create/', views.review_create),
    path('post/review/update/', views.review_update),
    path('post/review/delete/', views.review_delete),

    # Advertisement Event
    path('get/event/<slug:first>/<slug:second>/<slug:ad_id>/', views.event_get),
    path('post/event/create/', views.event_create),
    path('post/event/update/', views.event_update),
    path('post/event/delete/', views.event_delete),

    # Advertisement Images
    path('get/advertisement/images/<slug:first>/<slug:second>/<slug:ad_pk>/', views.images_get),

    #---------------- Accommodation Seeker Views ----------------#


    #---------------- General Views ----------------#
    path('get/advertisement/', views.get_all_ads),
    path('get/advertisement/<slug:first>/<slug:second>/<int:ad_id>/', views.get_single_ad),

    #---------------- Search module views ----------------#


    # URLs for testing
    path('advertisement/<int:pk>/', views.advertisement_detail),
    path('user/<int:pk>/', views.user_detail),
    path('review/<int:pk>/', views.review_detail),
    path('event/<int:pk>/', views.event_detail),

    path('api/public/', views.public),
    path('api/private/', views.private),

    path('admin/', admin.site.urls),
]
