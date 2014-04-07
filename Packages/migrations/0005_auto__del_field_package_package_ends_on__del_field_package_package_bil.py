# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Package.package_ends_on'
        db.delete_column(u'Packages_package', 'package_ends_on')

        # Deleting field 'Package.package_billing_type'
        db.delete_column(u'Packages_package', 'package_billing_type')

        # Deleting field 'Package.package_type'
        db.delete_column(u'Packages_package', 'package_type')

        # Deleting field 'Package.package_changed_on'
        db.delete_column(u'Packages_package', 'package_changed_on')

        # Adding field 'Package.type'
        db.add_column(u'Packages_package', 'type',
                      self.gf('django.db.models.fields.CharField')(default='I', max_length='20'),
                      keep_default=False)

        # Adding field 'Package.changed_on'
        db.add_column(u'Packages_package', 'changed_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Package.ends_on'
        db.add_column(u'Packages_package', 'ends_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Package.billing_type'
        db.add_column(u'Packages_package', 'billing_type',
                      self.gf('django.db.models.fields.CharField')(default=('3', '3 Months'), max_length='20'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Package.package_ends_on'
        db.add_column(u'Packages_package', 'package_ends_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Package.package_billing_type'
        db.add_column(u'Packages_package', 'package_billing_type',
                      self.gf('django.db.models.fields.CharField')(default=('3', '3 Months'), max_length='20'),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Package.package_type'
        raise RuntimeError("Cannot reverse this migration. 'Package.package_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Package.package_type'
        db.add_column(u'Packages_package', 'package_type',
                      self.gf('django.db.models.fields.CharField')(max_length='20'),
                      keep_default=False)

        # Adding field 'Package.package_changed_on'
        db.add_column(u'Packages_package', 'package_changed_on',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Package.type'
        db.delete_column(u'Packages_package', 'type')

        # Deleting field 'Package.changed_on'
        db.delete_column(u'Packages_package', 'changed_on')

        # Deleting field 'Package.ends_on'
        db.delete_column(u'Packages_package', 'ends_on')

        # Deleting field 'Package.billing_type'
        db.delete_column(u'Packages_package', 'billing_type')


    models = {
        u'Packages.package': {
            'Meta': {'object_name': 'Package'},
            'billing_type': ('django.db.models.fields.CharField', [], {'default': "('3', '3 Months')", 'max_length': "'20'"}),
            'changed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ends_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "('0', 'NOT-PAID')", 'max_length': "'20'"}),
            'purchased_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'package'", 'unique': 'True', 'to': u"orm['Users.User']"})
        },
        u'Users.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'mobile': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Packages']