# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Text'
        db.create_table('texts_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal('texts', ['Text'])

        # Adding model 'Paragraph'
        db.create_table('texts_paragraph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Text'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('texts', ['Paragraph'])


    def backwards(self, orm):
        
        # Deleting model 'Text'
        db.delete_table('texts_text')

        # Deleting model 'Paragraph'
        db.delete_table('texts_paragraph')


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
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['texts']
