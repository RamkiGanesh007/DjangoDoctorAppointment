# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210203_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='gender',
            field=models.CharField(max_length=1, default='Unknown', choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_addinfo',
            field=models.TextField(verbose_name='Your Additional Info Here: ', max_length=200, default='No Info'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_email',
            field=models.EmailField(verbose_name='Your Email Address:', max_length=40, default='unknown@gmail.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_mobile',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(verbose_name='Choose a doctor:', on_delete=django.db.models.deletion.DO_NOTHING, to='appointments.Doctor'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=True),
        ),
    ]
