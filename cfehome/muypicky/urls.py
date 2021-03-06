"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView

from restaurants.views import (
     HomeView, home_function, home_base, about, ContactView,
     restaurant_listview, restaurant_createview, restaurant_createview_wrong_way,

     )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home_function$', home_function), # function based view
    url(r'^home_base$', home_base),
    url(r'^$', HomeView.as_view()),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^restaurants_listview/$', restaurant_listview),
    url(r'^restaurants/create_function/$', restaurant_createview),
    url(r'^restaurants/create_wrong_way/$', restaurant_createview_wrong_way),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),


]
