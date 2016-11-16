from django.conf.urls import include, url
from .views import WebIndex, SnippetsList

urlpatterns = [
    url(r'^$',
      WebIndex.as_view(),
      name='index'), 
    url(r'^listado/$',
      SnippetsList.as_view(),
      name='list'), 
]
