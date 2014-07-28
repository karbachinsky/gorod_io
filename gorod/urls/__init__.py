"""
    Base gorod urls
"""

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from gorod.views import base, user, complaint
from gorod.utils.sitemap import sitemaps

urlpatterns = patterns('',
    # Project main page
    url(r'^$', base.IndexView.as_view(), name='index'),

    # User profile
    url(r'^logout/?$', user.LogoutView.as_view(), name='logout'),

    # Captcha
    url(r'^captcha/', include('captcha.urls')),

    ## API urls
    url(r'^api/', include('gorod.urls.api', namespace='gorodapi')),

    # Sitemap.xml
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}, name='sitemap'),

    ## Static pages
    url(r'^rules/?', TemplateView.as_view(template_name="gorod/rules.html"), name='rules'),

    # Complaint add
    url(r'^complaint/?', complaint.ComplaintAddView.as_view(), name='complaint'),

    # One City pages
    url(r'^(?P<city_name>\w+)/', include('gorod.urls.city', namespace='gorod')),
)

