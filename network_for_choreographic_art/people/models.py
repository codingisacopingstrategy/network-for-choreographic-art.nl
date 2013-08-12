from django.db import models

class Profile(models.Model):
    headline = models.CharField(max_length=255)
    user = models.OneToOneField('auth.User')
    def __unicode__(self):
        return "%s" % (self.user.get_full_name())
      