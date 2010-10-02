import datetime
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation
from tweetar import *
from djtweetar.runlogs.models import TweetarRun

def send_reports():
    profiles = TwitterProfile.objects.filter(content_type=ContentType.objects.get_for_model(WeatherStation))

    exception_count = 0
    run = TweetarRun(begin=datetime.datetime.now())

    for profile in profiles:
        conf = {
            'station': profile.content_object.code,
            'twitter_user': profile.screenname,
            'oauth_consumer_key': settings.TWITTER_CONSUMER_KEY,
            'oauth_consumer_secret': settings.TWITTER_CONSUMER_SECRET_KEY,
            'access_token_key': profile.consumer_key,
            'access_token_secret': profile.consumer_secret,
        }
        try:
            retrieve_and_post(conf)
        except urllib2.HTTPError:
            exception_count = exception_count + 1

    run.total_stations = len(profiles)
    run.stations_updated = 0 # need to update retrieve and post to return if it posted or not
    run.station_exceptions = exception_count
    run.end = datetime.datetime.now()
    run.save()

if __name__ == '__main__':
    send_reports()
