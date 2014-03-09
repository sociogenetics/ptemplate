# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin

from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    (r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/filebrowser/', include(site.urls)),

    (r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # XDP-page
    url(r'^', include('xendor.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
