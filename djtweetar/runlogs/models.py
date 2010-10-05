from django.db import models
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation

class TweetarRun(models.Model):
    begin = models.DateTimeField()
    end = models.DateTimeField()
    elapsed_seconds = models.PositiveIntegerField()
    total_stations = models.PositiveIntegerField()
    stations_updated = models.PositiveIntegerField()
    station_exceptions = models.PositiveIntegerField()

    def __unicode__(self):
        return u'Ran for %s seconds for %s stations; %s updated; %s exceptions' % (self.elapsed_seconds, self.total_stations, self.stations_updated, self.station_exceptions)

    def save(self, *args, **kwargs):
        self.elapsed_seconds = (self.end - self.begin).seconds
        super(TweetarRun, self).save(*args, **kwargs)

class TweetarException(models.Model):
    run = models.ForeignKey(TweetarRun)
    station = models.ForeignKey(WeatherStation)
    profile = models.ForeignKey(TwitterProfile)
    exception = models.TextField(blank=True)
    metar_from_noaa = models.CharField(max_length=256, blank=True)
    last_twitter_post = models.CharField(max_length=256, blank=True)
    metar_posted = models.BooleanField(default=False)
    addressed = models.BooleanField(default=False)
