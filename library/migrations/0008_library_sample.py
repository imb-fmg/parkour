# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_load_concentration_methods_and_sequencing_run_conditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('concentration', models.FloatField(verbose_name='Concentration')),
                ('dna_dissolved_in', models.CharField(max_length=200, verbose_name='DNA Dissolved in')),
                ('sample_volume', models.IntegerField(verbose_name='Sample Volume')),
                ('equal_representation_nucleotides', models.BooleanField()),
                ('sequencing_depth', models.IntegerField(verbose_name='Sequencing Depth')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('enrichment_cycles', models.IntegerField(verbose_name='No. of Enrichment Cycles')),
                ('index_reads', models.IntegerField(verbose_name='Index Reads')),
                ('index_i7', models.CharField(blank=True, max_length=200, null=True, verbose_name='Index I7')),
                ('index_i5', models.CharField(blank=True, max_length=200, null=True, verbose_name='Index I5')),
                ('mean_fragment_size', models.IntegerField(verbose_name='Mean Fragment Size')),
                ('qpcr_result', models.FloatField(blank=True, null=True, verbose_name='qPCR Result')),
                ('concentration_determined_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.ConcentrationMethod', verbose_name='Concentration Determined by')),
                ('index_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.IndexType', verbose_name='Index Type')),
                ('library_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryProtocol', verbose_name='Library Protocol')),
                ('library_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryType', verbose_name='Library Type')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Organism', verbose_name='Organism')),
                ('sequencing_run_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.SequencingRunCondition', verbose_name='Sequencing Run Condition')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
                'verbose_name': 'Library',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('concentration', models.FloatField(verbose_name='Concentration')),
                ('dna_dissolved_in', models.CharField(max_length=200, verbose_name='DNA Dissolved in')),
                ('sample_volume', models.IntegerField(verbose_name='Sample Volume')),
                ('equal_representation_nucleotides', models.BooleanField()),
                ('sequencing_depth', models.IntegerField(verbose_name='Sequencing Depth')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('concentration_determined_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.ConcentrationMethod', verbose_name='Concentration Determined by')),
                ('library_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryProtocol', verbose_name='Library Protocol')),
                ('library_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.LibraryType', verbose_name='Library Type')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Organism', verbose_name='Organism')),
                ('sequencing_run_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.SequencingRunCondition', verbose_name='Sequencing Run Condition')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
