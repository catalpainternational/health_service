from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

if settings.DEBUG == True:
    urlpatterns = patterns('',
        # Using this to serve static content under the dev server
        (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATICFILES_ROOT}),
    )
