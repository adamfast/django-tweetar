from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from djtweetar.stations.forms import *
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation
from tweetar import *

def main(request):
    form = StationRegistrationForm()
    return render_to_response('home.html', {'form': form,}, context_instance=RequestContext(request))

def add(request):
    ws = None

    if request.method == 'POST':
        form = StationRegistrationForm(request.POST)

        if form.is_valid():
            ws = WeatherStation.objects.filter(code__icontains=form.cleaned_data['code'])
            if ws.count() == 1:
                return HttpResponseRedirect(reverse('station', args=[ws[0].code]))
    else:
        form = StationRegistrationForm()

    return render_to_response('add.html', {'form': form, 'ws': ws}, context_instance=RequestContext(request))

def add2(request, station=None):
    if not station:
        return HttpResponseRedirect(reverse('submit_form'))
    else:
        ws = WeatherStation.objects.get(code=station)
        try:
            tp = TwitterProfile.objects.get(content_type=ContentType.objects.get_for_model(WeatherStation), object_id=ws.id)
        except TwitterProfile.DoesNotExist:
            tp = None

    request.session['next'] = reverse('station', args=[ws.code])

    return render_to_response('add2.html', {'ws': ws, 'tp': tp, 'socialregistration_connect_object': ws}, context_instance=RequestContext(request))

def connect(request, station):
    station = get_object_or_404(Station, code=station)

    return render_to_response('connect.html', {'socialregistration_connect_object': station,}, context_instance=RequestContext(request))

def auto_tweet(sender, **kwargs):
    """Run when a socialprofile is saved - on this site, that should only be on initial creation."""
    profile = kwargs['instance']

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

post_save.connect(auto_tweet, sender=TwitterProfile)
