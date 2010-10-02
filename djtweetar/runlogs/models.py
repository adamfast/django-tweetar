from django.db import models

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
