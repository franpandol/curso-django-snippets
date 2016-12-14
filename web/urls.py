from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from .views import WebIndex, AboutUs

urlpatterns = [
    url(r'^$',
        WebIndex.as_view(),
        name='index'),
    url(r'^about_us/$',
        AboutUs.as_view(),
        name='about-us'),
]