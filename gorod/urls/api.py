"""
    gorod API urls
"""

from django.conf.urls import patterns, url

from gorod.views import articles


urlpatterns = patterns('',
    url(r'feed/?$', articles.FeedAPIView.as_view(), name='api-feed'),
)
