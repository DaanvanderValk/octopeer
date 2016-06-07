# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 11:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20160603_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('dom', models.TextField()),
                ('created_at', unixtimestampfield.fields.UnixTimeStampField(default=0.0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session')),
            ],
            options={
                'db_table': 'html_page',
            },
        ),
    ]