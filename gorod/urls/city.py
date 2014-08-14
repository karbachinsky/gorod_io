from django.conf.urls import patterns, url

from gorod.views import base, organizations, hub, user, articles, redirects, city_welcome

urlpatterns = patterns('',
    # Main page    
    #url(r'^$', views.index, name='index'),
    #url(r'^town/(?P<city>\w+)/?$', RedirectView.as_view(url='/town/kashin'), name='index'),
    #url(r'^$', RedirectView.as_view(url='/town/kashin'), name='index'),

    # City main page
    url(r'^$', articles.FeedView.as_view(), name='city_main_page'),

    url(r'^welcome/?$', city_welcome.CityWelcomeView.as_view(), name='welcome'),

    # City feed page. The same as main page
    #url(r'^feed/?$', articles.FeedView.as_view(), name='feed'),

    ## Organzations

    # Organizations list page
    url(r'^org/?$', organizations.OrganizationsView.as_view(), name='organizations'),
    # One organization page
    url(r'^org/(?P<organization_id>\d+)/?$', organizations.OrganizationView.as_view(), name='organization'),


    ## City info/about
    url(r'^hub/?$', hub.HubView.as_view(), name='hub'),
    url(r'^hub/(?P<question_id>\d+)/?$', hub.HubQuestionView.as_view(), name='hub-question'),

    ## City user
    url(r'^user/(?P<user_id>\d+)/?$', user.ProfileView.as_view(), name='user'),

    ### Some old redirects to new urls during url fixes
    url(r'^organization/(?P<organization_id>\d+)/?$', redirects.OrganizationRedirectView.as_view()),
    url(r'^article/(?P<article_id>\d+)/?$', redirects.ArticleRedirectView.as_view()),

    ## Articles

    # One article page
    url(r'^(?P<rubric_name>\w+)/(?P<article_id>\d+)/?$', articles.ArticleView.as_view(), name='article'),
    # Rubric feed list page
    url(r'^(?P<rubric_name>\w+)/?$', articles.FeedView.as_view(), name='feed-rubric'),

    ## Ajax urls

    # Add article by user
    url(r'^ajax/(?P<rubric_name>\w+)/add/?$', articles.ArticleAddView.as_view(), name='article-add'),
    # Delete article by user
    url(r'^ajax/article/delete/(?P<article_id>\d+)/?$', articles.ArticleDeleteView.as_view(), name='article-delete'),

)

