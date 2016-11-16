from django.conf.urls import include, url
from .views import WebIndex, SnippetsList, SnippetsDetail


urlpatterns = [
    url(r'^$',
        WebIndex.as_view(),
        name='index'),
    url(r'^listado/$',
        SnippetsList.as_view(),
        name='list'),
    url(r'^(?P<pk>\d+)/$',
        SnippetsDetail.as_view(),
        name='detail'),
]
