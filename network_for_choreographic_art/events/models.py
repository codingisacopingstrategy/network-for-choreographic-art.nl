import datetime

from django.db import models
from django.template.defaultfilters import slugify
from network_for_choreographic_art.texts.models import Text

class Event(models.Model):
    """Event"""
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, editable=False)

    date = models.DateField(blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    stop_date_time = models.DateTimeField(blank=True, null=True)
    
    owner = models.ForeignKey('auth.User',blank=True, null=True, related_name='owner')
    attendees = models.ManyToManyField('auth.User', blank=True, related_name='attendees')

    photoset = models.CharField(max_length=255, blank=True, null=True)

    texts = models.ManyToManyField(Text, blank=True, null=True, related_name='event_minutes')
    
    def is_future(self):
        return self.start >= datetime.datetime.now()

    def __unicode__(self):
        return "%s" % (self.slug)

    def organised(self):
      return self.owner.username != "eric"

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        ''' Automatically generate the slug from the title '''
        self.slug = slugify(self.title)
        super(Event, self).save(force_insert, force_update)

