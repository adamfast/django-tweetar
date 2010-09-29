from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from djtweetar.stations.forms import *
from socialregistration.models import TwitterProfile
from weathertracking.models import WeatherStation

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
                return HttpResponseRedirect('%s?code=%s' % (reverse('step2'), ws[0].code))
    else:
        form = StationRegistrationForm()

    return render_to_response('add.html', {'form': form, 'ws': ws}, context_instance=RequestContext(request))

def add2(request):
    if not request.GET.get('code'):
        return HttpResponseRedirect(reverse('submit_form'))
    else:
        ws = WeatherStation.objects.get(code=request.GET.get('code'))
        try:
            tp = TwitterProfile.objects.get(content_type=ContentType.objects.get_for_model(WeatherStation), object_id=ws.id)
        except TwitterProfile.DoesNotExist:
            tp = None

    request.session['next'] = '%s?code=%s' % (reverse('step2'), ws.code)

    return render_to_response('add2.html', {'ws': ws, 'tp': tp, 'socialregistration_connect_object': ws}, context_instance=RequestContext(request))

def connect(request, station):
    station = get_object_or_404(Station, code=station)

    return render_to_response('connect.html', {'socialregistration_connect_object': station,}, context_instance=RequestContext(request))
