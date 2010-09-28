from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djtweetar/', include('djtweetar.foo.urls')),

    (r'^connect-site/(?P<station>[a-zA-Z0-9*.]+)/$', 'djtweetar.stations.views.connect'),

    (r'^socialregistration/', include('socialregistration.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
