# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150104_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('event', models.ForeignKey(related_name='marks', to='event.Event')),
            ],
            options={
                'verbose_name': 'Event mark',
                'verbose_name_plural': 'Event marks',
            },
            bases=(models.Model,),
        ),
    ]
