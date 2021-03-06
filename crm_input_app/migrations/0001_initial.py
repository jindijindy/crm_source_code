# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParaSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_fail_id', models.CharField(help_text='Control Failure ID', max_length=15, verbose_name='Control Failure ID')),
                ('asset_id', models.CharField(help_text='Asset ID', max_length=15, verbose_name='Asset ID')),
                ('control_name', models.CharField(help_text='Control Name', max_length=100, verbose_name='Control Name')),
                ('ctr_fail_desc', models.CharField(help_text='Control Failure Description', max_length=600, verbose_name='Control Failure Description')),
                ('sensitive_data', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='Sensitive Data', max_length=1, verbose_name='Sensitive Data')),
                ('asset_loc', models.CharField(choices=[('1', 'National Data Center'), ('2', 'Regional'), ('3', 'Server Room'), ('4', 'Exposed'), ('5', 'Vendor Hosted')], help_text='Asset Location', max_length=1, verbose_name='Asset Location')),
                ('solution_prov', models.CharField(choices=[('1', 'Reputable Vendor'), ('2', 'Not Reputable Vendor'), ('3', 'Mature Internal Team (Certified)')], help_text='Solution Provider', max_length=1, verbose_name='Solution Provider')),
                ('pocs', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='Point of Care System', max_length=1, verbose_name='Point of Care System')),
                ('auth_meth', models.CharField(choices=[('1', 'Anonymous (n/a)'), ('2', 'Local'), ('3', 'Central')], help_text='Authentication Method', max_length=1, verbose_name='Authentication Method')),
                ('cri_met', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='All criteria  well maintained are met', max_length=1, verbose_name='All criteria  well maintained are met')),
                ('wide_vul', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='Widely known vulnerability', max_length=1, verbose_name='Widely known vulnerability')),
                ('comp_ctr', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='There is a compensating control', max_length=1, verbose_name=' There is a compensating control')),
                ('internet_exp', models.CharField(choices=[('1', 'Yes'), ('0', 'No')], help_text='Internet Exposed or in DMZ', max_length=1, verbose_name='Internet Exposed or in DMZ')),
            ],
        ),
    ]
