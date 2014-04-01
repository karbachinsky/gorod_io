from django.conf.urls import patterns, url

from django.views.generic.base import RedirectView

from gorod.views import base, organizations

urlpatterns = patterns('',
    # Main page    
    #url(r'^$', views.index, name='index'),
    #url(r'^town/(?P<city>\w+)/?$', RedirectView.as_view(url='/town/kashin'), name='index'),
    #url(r'^$', RedirectView.as_view(url='/town/kashin'), name='index'),

    url(r'^$', base.index, name='index'),
    # City main page
    url(r'^town/(?P<city>\w+)/feed/?$', base.feed, name='feed'),
    # Article(s)
    url(r'^article/(?P<article_id>\d+)/?$', base.article, name='article'),
    # Organzation(s)
    url(r'^town/(?P<city>\w+)/organizations/?$', organizations.organizations, name='organizations'),
    url(r'^organization/(?P<organization_id>\d+)/?$', organizations.organization, name='organization'),

    url(r'^town/(?P<city>\w+)/?', base.feed, name='city'),
)

