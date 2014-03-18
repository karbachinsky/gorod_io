from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gorod_io.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/?', include(admin.site.urls)),
    #url(r'^tinymce/?', include('tinymce.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('gorod.urls', namespace='gorod'))
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
