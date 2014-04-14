from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^admin/?', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('gorod.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

#handler404 = 'gorod.views.handler404'
#handler500 = 'gorod.views.handler500'

