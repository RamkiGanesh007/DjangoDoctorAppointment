# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20210202_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(verbose_name='Choose an Appointment date and time:'),
        ),
    ]
