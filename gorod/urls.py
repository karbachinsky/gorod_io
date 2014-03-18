from django.conf.urls import patterns, url

from django.views.generic.base import RedirectView

from gorod import views

urlpatterns = patterns('',
    # Main page    
    #url(r'^$', views.index, name='index'),
    #url(r'^town/(?P<city>\w+)/?$', RedirectView.as_view(url='/town/kashin'), name='index'),
    #url(r'^$', RedirectView.as_view(url='/town/kashin'), name='index'),
    url(r'^$', views.index, name='index'),
    # City main page
    url(r'^town/(?P<city>\w+)/feed/?$', views.feed, name='feed'),
    # Article(s)
    url(r'^article/(?P<article_id>\d+)/?$', views.article, name='article'),
    # Organzation(s)
    url(r'^town/(?P<city>\w+)/organizations/?$', views.organizations, name='organizations'),
    url(r'^organization/(?P<organization_id>\d+)/?$', views.organization, name='organization'),

    url(r'^town/(?P<city>\w+)/?', views.feed, name='city'),
)

