from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'url.views.index'),
        (r'^redirect$', 'url.views.redirect'),
	(r'^(.+)$','url.views.link'),
#	(r'^statics/(?P<path>.*)$', 'django.views.static.serve',
 #       {'document_root': settings.STATIC_DOC_ROOT}),
        (r'^admin/', include(admin.site.urls))
        )
	

