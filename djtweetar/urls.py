from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djtweetar/', include('djtweetar.foo.urls')),

    url(r'^add/$', 'djtweetar.stations.views.add', name='submit_form'),
    url(r'^add2/$', 'djtweetar.stations.views.add2', name='step2'),
    (r'^connect-site/(?P<station>[a-zA-Z0-9*.]+)/$', 'djtweetar.stations.views.connect'),

    url(r'^stations/(?P<station>[a-zA-Z0-9*.]+)/$', 'djtweetar.stations.views.add2', name='station'),

    (r'^socialregistration/', include('socialregistration.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'djtweetar.stations.views.main'),
)
