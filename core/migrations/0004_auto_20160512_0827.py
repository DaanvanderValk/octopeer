# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160427_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'element_type',
            },
        ),
        migrations.CreateModel(
            name='KeystrokeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('keystroke', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'keystroke_event',
            },
        ),
        migrations.CreateModel(
            name='MouseClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'mouse_click_event',
            },
        ),
        migrations.CreateModel(
            name='MousePositionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('viewport_x', models.IntegerField()),
                ('viewport_y', models.IntegerField()),
            ],
            options={
                'db_table': 'mouse_position_event',
            },
        ),
        migrations.CreateModel(
            name='MouseScrollEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('viewport_x', models.IntegerField()),
                ('viewport_y', models.IntegerField()),
            ],
            options={
                'db_table': 'mouse_scroll_event',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'repository',
            },
        ),
        migrations.CreateModel(
            name='SemanticEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField()),
                ('duration', models.PositiveIntegerField()),
                ('element_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ElementType')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.EventType')),
            ],
            options={
                'db_table': 'semantic_event',
            },
        ),
        migrations.CreateModel(
            name='WindowResolutionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            options={
                'db_table': 'window_resolution',
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='session',
        ),
        migrations.RemoveField(
            model_name='pullrequest',
            name='closed_at',
        ),
        migrations.RemoveField(
            model_name='pullrequest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pullrequest',
            name='merged_at',
        ),
        migrations.RemoveField(
            model_name='session',
            name='platform',
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='pull_request_number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventposition',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SemanticEvent'),
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='windowresolutionevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='semanticevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='mousescrollevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='mousepositionevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='mouseclickevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='keystrokeevent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Session'),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='repository',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Repository'),
        ),
    ]
