from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    # Auth
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^', include('gorod.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#handler404 = 'gorod.views.handler404'
#handler500 = 'gorod.views.handler500'

