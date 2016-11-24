from django.conf.urls import include, url
from .views import (
    WebIndex,
    SnippetsList, 
    SnippetsDetail, 
    SnippetsAlta,
    AboutUs,
    SnippetsActualizar,
    SnippetsListTable
)

urlpatterns = [
    
    url(r'^$',
        WebIndex.as_view(),
        name='index'),

    url(r'^listado/$',
        SnippetsList.as_view(),
        name='list'),

    url(r'^listado_tablas/$',
        SnippetsListTable.as_view(),
        name='list-table'),

    url(r'^about_us/$',
        AboutUs.as_view(),
        name='about-us'),

    url(r'^alta/$',
        SnippetsAlta.as_view(),
        name='alta'
    ),

    url(r'^(?P<pk>\d+)/actualizar/$',
        SnippetsActualizar.as_view(),
        name='edit'
    ),

    url(r'^(?P<pk>\d+)/$',
        SnippetsDetail.as_view(),
        name='detail'),
]
