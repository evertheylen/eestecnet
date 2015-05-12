# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import common.util


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('applicable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Applicable')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.applicable', common.util.Reversable),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('baseevent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='ParticipationConfirmation',
            fields=[
                ('confirmation_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='common.Confirmation')),
                ('confirmable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Confirmable')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.confirmable', 'common.confirmation', object),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('baseevent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('baseevent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.BaseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.baseevent',),
        ),
    ]
