from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    function = models.CharField(max_length=120)
    join_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.full_name

class Vote(models.Model):
    pub_date = models.DateTimeField()
    voter = models.ForeignKey(User)

    def __unicode__(self):
        return self.voter.full_name