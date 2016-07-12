# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_input_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paraset',
            name='asset_id',
            field=models.CharField(max_length=15, verbose_name='Asset ID'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='asset_loc',
            field=models.CharField(choices=[('1', 'National Data Center'), ('2', 'Regional'), ('3', 'Server Room'), ('4', 'Exposed'), ('5', 'Vendor Hosted')], max_length=1, verbose_name='Asset Location'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='auth_meth',
            field=models.CharField(choices=[('1', 'Anonymous (n/a)'), ('2', 'Local'), ('3', 'Central')], max_length=1, verbose_name='Authentication Method'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='comp_ctr',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name=' There is a compensating control'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='control_fail_id',
            field=models.CharField(max_length=15, verbose_name='Control Failure ID'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='control_name',
            field=models.CharField(max_length=100, verbose_name='Control Name'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='cri_met',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='All criteria  well maintained are met'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='ctr_fail_desc',
            field=models.CharField(max_length=600, verbose_name='Control Failure Description'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='internet_exp',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='Internet Exposed or in DMZ'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='pocs',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='Point of Care System'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='sensitive_data',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='Sensitive Data'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='solution_prov',
            field=models.CharField(choices=[('1', 'Reputable Vendor'), ('2', 'Not Reputable Vendor'), ('3', 'Mature Internal Team (Certified)')], max_length=1, verbose_name='Solution Provider'),
        ),
        migrations.AlterField(
            model_name='paraset',
            name='wide_vul',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, verbose_name='Widely known vulnerability'),
        ),
    ]