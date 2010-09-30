from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation
from tweetar import *

def send_reports():
    profiles = TwitterProfile.objects.filter(content_type=ContentType.objects.get_for_model(WeatherStation))

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
            pass

if __name__ == '__main__':
    send_reports()
