""" Base gorod urls """

from django.conf.urls import patterns, include, url

from gorod.views import base, user


urlpatterns = patterns('',
    # User profile
    url(r'^logout/?$', user.logout_view, name='logout'),

    # One City pages
    url(r'^town/(?P<city_name>\w+)/', include('gorod.urls.city', namespace='gorod')),

    # Project main page
    url(r'^$', base.index, name='index')
)

