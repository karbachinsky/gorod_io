from django.conf.urls import patterns, url

from django.views.generic.base import RedirectView

from gorod.views import base, organizations, city_info

urlpatterns = patterns('',
    # Main page    
    #url(r'^$', views.index, name='index'),
    #url(r'^town/(?P<city>\w+)/?$', RedirectView.as_view(url='/town/kashin'), name='index'),
    #url(r'^$', RedirectView.as_view(url='/town/kashin'), name='index'),

    # City main page
    url(r'^$', base.feed, name='city_main_page'),

    # City feed page. The same as main page
    url(r'^feed/?$', base.feed, name='feed'),

    ## Articles

    # One article page
    url(r'^article/(?P<article_id>\d+)/?$', base.article, name='article'),
    # Rubric feed list page 
    url(r'^feed/rubric/(?P<rubric_name>\w+)/?$', base.feed, name='feed-rubric'),

    ## Organzations

    # Organizations list page
    url(r'^organizations/?$', organizations.organizations, name='organizations'),
    # One organization page
    url(r'^organization/(?P<organization_id>\d+)/?$', organizations.organization, name='organization'),

    ## City info/about
    url(r'^info/?$', city_info.info, name='city-info'),
)

