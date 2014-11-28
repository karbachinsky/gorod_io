from django.conf.urls import patterns, url

from gorod.views import base, user, articles, redirects

urlpatterns = patterns('',
    # City main page
    url(r'^$', articles.GroupsView.as_view(), name='city-main-page'),

    ## City user
    url(r'^user/(?P<user_id>\d+)/?$', user.ProfileView.as_view(), name='user'),

    ### Some old redirects to new urls during url fixes
    url(r'^article/(?P<article_id>\d+)/?$', redirects.ArticleRedirectView.as_view()),

    ## Ajax urls

    # Add article by user
    url(r'^article/add/?$', articles.ArticleAddView.as_view(), name='article-add'),
    # Edit article by user
    url(r'^(?P<rubric_name>[\w_-]+)/edit/(?P<article_id>\d+)/?$', articles.ArticleEditView.as_view(), name='article-edit'),
    # Delete article by user
    url(r'^article/delete/(?P<article_id>\d+)/?$', articles.ArticleDeleteView.as_view(), name='article-delete'),

    ## Articles

    # One article page
    url(r'^(?P<rubric_name>[\w_-]+)/(?P<article_id>\d+)/?$', articles.ArticleView.as_view(), name='article'),
    # Rubric feed list page
    url(r'^(?P<rubric_name>[\w_-]+)/?$', articles.FeedView.as_view(), kwargs={'filter_name': 'last'}, name='feed-rubric'),
    # Rubric feed list page with filter
    url(r'^(?P<rubric_name>[\w_-]+)/(?P<filter_name>\w+)/?$', articles.FeedView.as_view(), name='feed-rubric-filter'),

)

