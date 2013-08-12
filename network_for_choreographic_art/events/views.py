# Create your views here.
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from network_for_choreographic_art.events.models import Event
from network_for_choreographic_art.texts.models import Text
import datetime

def index(request):
    upcoming_events = Event.objects.filter(date__gte=datetime.date.today())
    past_events = Event.objects.filter(date__lt=datetime.date.today())
    suggested_events = Event.objects.filter(date__isnull=True)
    events = sorted(Event.objects.all().order_by('id'), key=lambda event: event.attendees.count(), reverse=True)
    return render_to_response('events.html',
    {'slug': 'events', 'events' : events, 'upcoming_events' : upcoming_events, 'past_events': past_events, 'suggested_events' : suggested_events},
    context_instance=RequestContext(request))

def info(request):
    events = Event.objects.all().order_by('id')
    return render_to_response('info.html',{'slug': 'events', 'events' : events},context_instance=RequestContext(request))

def event(request, slug):
    photos = None
    text = None
    event = get_object_or_404(Event, slug=slug)
    if event.photoset:
        import facebook
        graph = facebook.GraphAPI('115359248549515|i3BaoPsl84wL2NlR26BMSpQuYCQ')
        photos = graph.get_connections(event.photoset, 'photos', limit=50)['data']
    return render_to_response('event.html',{ 'slug' : "event_%s" % slug , 'photoset' : photos, 'event' : event},context_instance=RequestContext(request))
    
@login_required
def join(request, slug):
    user = request.user
    event = get_object_or_404(Event, slug=slug)
    event.attendees.add(user)
    event.save()
    return HttpResponseRedirect('/events/#%s' % slug)

@login_required
def organise(request, slug):
    user = request.user
    event = get_object_or_404(Event, slug=slug)
    if request.method == 'POST':
        date = map(int,request.POST['date'].split('/'))
        event.date = datetime.date(date[2],date[1],date[0])
        event.location = request.POST['location']
        event.description = request.POST['description']
        event.owner = user
        event.save()
        return HttpResponseRedirect('/events/#%s' % slug)
    return render_to_response('organise.html',{'slug': 'events-organise', 'event' : event},context_instance=RequestContext(request))

