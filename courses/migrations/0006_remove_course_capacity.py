# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-12-10 04:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_section_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='capacity',
        ),
    ]