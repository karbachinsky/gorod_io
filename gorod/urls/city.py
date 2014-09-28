from django.conf.urls import patterns, url

from gorod.views import base, organizations, hub, user, articles, redirects, city_welcome, payment

urlpatterns = patterns('',
    # City main page
    url(r'^$', articles.FeedView.as_view(), name='city-main-page'),

    # City welcome
    url(r'^welcome/?$', city_welcome.CityWelcomeView.as_view(), name='welcome'),

    ## Organzations

    # Organizations list page
    url(r'^org/?$', organizations.OrganizationsView.as_view(), name='organizations'),
    # One organization page
    url(r'^org/(?P<organization_id>\d+)/?$', organizations.OrganizationView.as_view(), name='organization'),

    ## City hub
    url(r'^question/?$', hub.HubView.as_view(), name='hub'),
    url(r'^question/(?P<question_id>\d+)/?$', hub.HubQuestionView.as_view(), name='hub-question'),

    ## Payment
    url(r'^payment/?$', payment.PaymentsView.as_view(), name='payments'),

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
    url(r'^(?P<rubric_name>\w+)/add/?$', articles.ArticleAddView.as_view(), name='article-add'),
    # Edit article by user
    url(r'^(?P<rubric_name>\w+)/edit/(?P<article_id>\d+)/?$', articles.ArticleEditView.as_view(), name='article-edit'),
    # Delete article by user
    url(r'^article/delete/(?P<article_id>\d+)/?$', articles.ArticleDeleteView.as_view(), name='article-delete'),
)

