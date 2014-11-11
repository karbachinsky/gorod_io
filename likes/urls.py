from django.conf.urls import patterns, url
from likes import views

urlpatterns = patterns('',
    # add like
    url(r'^add/?', views.AddView.as_view(), name='like-add'),
)