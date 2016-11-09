from django.conf.urls import include, url
from .views import WebIndex

urlpatterns = [
    url(r'^$',
      WebIndex.as_view(),
      name='index'), 
]
