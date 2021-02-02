# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(verbose_name='Appointment date and time:'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(verbose_name='Choose a doctor:', to='appointments.Doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_middlename',
            field=models.CharField(verbose_name='Your middle name:', max_length=40),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(verbose_name='Your name:', max_length=40),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_surname',
            field=models.CharField(verbose_name='Your last name:', max_length=40),
        ),
    ]
