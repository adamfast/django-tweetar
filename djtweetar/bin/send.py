import datetime
import sys
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation
from tweetar import *
from djtweetar.runlogs.models import TweetarRun, TweetarException

def send_reports():
    profiles = TwitterProfile.objects.filter(content_type=ContentType.objects.get_for_model(WeatherStation))

    exception_count = 0
    run = TweetarRun.objects.create(begin=datetime.datetime.now(), end=datetime.datetime.now(), elapsed_stations=0, total_stations=0, stations_updated=0, station_exceptions=0)

    for profile in profiles:
        exception_occurred = False
        # create the exception so that info can be appended to it if something goes wrong
        te = TweetarException.objects.create(run=run, station=profile.content_object, profile=profile)

        conf = {
            'station': profile.content_object.code,
            'twitter_user': profile.screenname,
            'oauth_consumer_key': settings.TWITTER_CONSUMER_KEY,
            'oauth_consumer_secret': settings.TWITTER_CONSUMER_SECRET_KEY,
            'access_token_key': profile.consumer_key,
            'access_token_secret': profile.consumer_secret,
            'djtweetar_exception': te,
        }

        try:
            retrieve_and_post(conf)
        except:
            exception_count = exception_count + 1
            te.exception = '%s\n%s' % (sys.exc_info()[0], sys.exc_info()[1])
            te.save()

        if not exception_occurred:
            te.delete() # no exception happened, so don't keep it around. This kind of sucks but there's no other way to make sure you get the info from inside python-tweetar unless you do this.

    run.total_stations = len(profiles)
    run.stations_updated = 0 # need to update retrieve and post to return if it posted or not
    run.station_exceptions = exception_count
    run.end = datetime.datetime.now()
    run.save()

if __name__ == '__main__':
    send_reports()
