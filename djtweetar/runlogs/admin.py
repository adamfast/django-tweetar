from django.contrib import admin
from djtweetar.runlogs.models import *

class TweetarRunAdmin(admin.ModelAdmin):
    list_display = ('begin', 'end', 'elapsed_seconds', 'total_stations', 'stations_updated', 'station_exceptions')

class TweetarExceptionAdmin(admin.ModelAdmin):
    list_display = ('station', 'profile', 'metar_posted', 'addressed')
    list_filter = ('addressed', 'metar_posted')

admin.site.register(TweetarRun, TweetarRunAdmin)
admin.site.register(TweetarException, TweetarExceptionAdmin)
