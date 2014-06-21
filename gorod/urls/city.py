from django.conf.urls import patterns, url

from django.views.generic.base import RedirectView

from gorod.views import base, organizations, city_info, user, articles

urlpatterns = patterns('',
    # Main page    
    #url(r'^$', views.index, name='index'),
    #url(r'^town/(?P<city>\w+)/?$', RedirectView.as_view(url='/town/kashin'), name='index'),
    #url(r'^$', RedirectView.as_view(url='/town/kashin'), name='index'),

    # City main page
    url(r'^$', articles.FeedView.as_view(), name='city_main_page'),

    # City feed page. The same as main page
    url(r'^feed/?$', articles.FeedView.as_view(), name='feed'),

    ## Articles

    # One article page
    url(r'^article/(?P<article_id>\d+)/?$', articles.ArticleView.as_view(), name='article'),
    # Rubric feed list page 
    url(r'^feed/rubric/(?P<rubric_name>\w+)/?$', articles.FeedView.as_view(), name='feed-rubric'),
    # Add article by user
    url(r'^article/add/?$', articles.AddView.as_view(), name='article-add'),

    ## Organzations

    # Organizations list page
    url(r'^organizations/?$', organizations.OrganizationsView.as_view(), name='organizations'),
    # One organization page
    url(r'^organization/(?P<organization_id>\d+)/?$', organizations.OrganizationView.as_view(), name='organization'),

    ## City info/about
    url(r'^info/?$', city_info.CityInfoView.as_view(), name='city-info'),

    ## City user
    url(r'^user/(?P<user_id>\d+)/?$', user.ProfileView.as_view(), name='user'),

)

