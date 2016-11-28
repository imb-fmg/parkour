# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 10:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooling', '0002_librarypreparation'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryPreparationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='library_preparation/%Y/%m/%d/')),
            ],
        ),
        migrations.AddField(
            model_name='librarypreparation',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pooling.LibraryPreparationFile', verbose_name='File'),
        ),
    ]