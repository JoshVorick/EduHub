# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 06:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EduProvider',
            new_name='Provider',
        ),
        migrations.RenameModel(
            old_name='EduSource',
            new_name='Resource',
        ),
        migrations.RenameField(
            model_name='coveredtopic',
            old_name='edusource',
            new_name='resource',
        ),
        migrations.RenameField(
            model_name='requiredtopic',
            old_name='edusource',
            new_name='resource',
        ),
    ]