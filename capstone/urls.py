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
    path('api/public/', views.public),
    path('api/private/', views.private),

    path('admin/', admin.site.urls),

    path('get/user/<slug:first>/<slug:second>/', views.user_profile_get),
    path('post/user/<slug:first>/<slug:second>/update/', views.user_profile_post),
    path('post/userLoggedIn/<slug:first>/<slug:second>/', views.is_loggedIn),

    path('get/advertisement/<slug:first>/<slug:second>/', views.advertisement_get),
    path('post/advertisement/<slug:first>/<slug:second>/create/', views.advertisement_create),
    path('post/advertisement/<slug:first>/<slug:second>/<slug:accommodation_name>/update/', views.advertisement_post),
    path('post/advertisement/<slug:first>/<slug:second>/<slug:accommodation_name>/delete/', views.advertisement_delete),

    # URLs for testing
    path('advertisement/<int:pk>/', views.advertisement_detail),
    path('user/<int:pk>/', views.user_detail),

]
