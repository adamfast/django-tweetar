from django.contrib import admin
from djtweetar.runlogs.models import *

class TweetarRunAdmin(admin.ModelAdmin):
    list_display = ('begin', 'end', 'elapsed_seconds', 'total_stations', 'stations_updated', 'station_exceptions')

admin.site.register(TweetarRun, TweetarRunAdmin)
