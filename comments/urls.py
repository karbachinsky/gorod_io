from django.conf.urls import patterns, url, include
from comments.views import AddView

urlpatterns = patterns('',
    # New
    url(r'^add/?', AddView.as_view(), name='comments-add'),

    # old
    url(r'', include('django.contrib.comments.urls')),
)

