from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from djtweetar.stations.models import Station

def connect(request, station):
    station = get_object_or_404(Station, code=station)

    return render_to_response('connect.html', {'socialregistration_connect_object': station,}, context_instance=RequestContext(request))
