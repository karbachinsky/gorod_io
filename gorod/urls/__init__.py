"""
    Base gorod urls
"""

from django.conf.urls import patterns, include, url

from gorod.views import base, user

urlpatterns = patterns('',
    # Project main page
    url(r'^$', base.IndexView.as_view(), name='index'),

    # User profile
    url(r'^logout/?$', user.LogoutView.as_view(), name='logout'),

    # Captcha
    url(r'^captcha/', include('captcha.urls')),

    # One City pages
    url(r'^(?P<city_name>\w+)/', include('gorod.urls.city', namespace='gorod')),

    url('^towns/?$', base.IndexView.as_view())
)

