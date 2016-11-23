from django.conf.urls import include, url
from .views import WebIndex, SnippetsList, SnippetsDetail
from .views import AboutUs
urlpatterns = [
    
    url(r'^$',
        WebIndex.as_view(),
        name='index'),

    url(r'^listado/$',
        SnippetsList.as_view(),
        name='list'),

    
    url(r'^about_us/$',
        AboutUs.as_view(),
        name='about-us'),


    url(r'^(?P<pk>\d+)/$',
        SnippetsDetail.as_view(),
        name='detail'),
]
