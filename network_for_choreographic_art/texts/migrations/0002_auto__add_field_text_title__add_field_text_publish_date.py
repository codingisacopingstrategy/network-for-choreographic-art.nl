# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Text.title'
        db.add_column('texts_text', 'title', self.gf('django.db.models.fields.CharField')(default='Initial Proposal from the Network', max_length=255), keep_default=False)

        # Adding field 'Text.publish_date'
        db.add_column('texts_text', 'publish_date', self.gf('django.db.models.fields.DateField')(default=datetime.date(2011, 3, 30)), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Text.title'
        db.delete_column('texts_text', 'title')

        # Deleting field 'Text.publish_date'
        db.delete_column('texts_text', 'publish_date')


    models = {
        'texts.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['texts.Text']"})
        },
        'texts.text': {
            'Meta': {'object_name': 'Text'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['texts']
