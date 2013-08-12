from django.db import models

# Create your models here.

class Text(models.Model):
    slug = models.CharField(max_length=70)
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
        
    def __unicode__(self):
        return self.slug

class Paragraph(models.Model):
    text = models.ForeignKey(Text)
    content = models.TextField()
    
    def __unicode__(self):
        return self.text.slug + ' ' + str(self.id)