# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GipsyAdminMenu'
        db.create_table(u'dashboard_gipsyadminmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dashboard.GipsyAdminMenu'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'dashboard', ['GipsyAdminMenu'])


    def backwards(self, orm):
        # Deleting model 'GipsyAdminMenu'
        db.delete_table(u'dashboard_gipsyadminmenu')


    models = {
        u'dashboard.gipsyadminmenu': {
            'Meta': {'ordering': "['order']", 'object_name': 'GipsyAdminMenu'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.GipsyAdminMenu']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['dashboard']