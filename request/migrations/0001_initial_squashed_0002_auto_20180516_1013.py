# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-16 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import request.models


class Migration(migrations.Migration):

    replaces = [('request', '0001_initial'), ('request', '0002_auto_20180516_1013')]

    dependencies = [
        ('library', '0001_initial'),
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('file', models.FileField(upload_to='request_files/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Name')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('description', models.TextField()),
                ('deep_seq_request', models.FileField(blank=True, null=True, upload_to='deep_sequencing_requests/%Y/%m/%d/', verbose_name='Deep Sequencing Request')),
                ('files', models.ManyToManyField(blank=True, related_name='request', to='request.FileRequest')),
                ('libraries', models.ManyToManyField(blank=True, related_name='request', to='library.Library')),
                ('samples', models.ManyToManyField(blank=True, related_name='request', to='sample.Sample')),
                ('user', models.ForeignKey(on_delete=models.SET(request.models.get_sentinel_user), to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Update Time')),
                ('samples_submitted', models.BooleanField(default=False, verbose_name='Samples Submitted')),
                ('sequenced', models.BooleanField(default=False, verbose_name='Sequenced')),
                ('cost_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.CostUnit', verbose_name='Cost Unit')),
            ],
        ),
    ]
