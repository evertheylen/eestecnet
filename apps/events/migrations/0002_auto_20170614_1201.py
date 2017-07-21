# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('feedback', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizing_committee',
            field=models.ManyToManyField(to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='questionaire',
            field=models.ForeignKey(related_name='eventstwo', blank=True, to='feedback.QuestionSet', help_text=b'Optional: If you want your participants to answer more questions other than writing about their motivation, you can include it here', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='questionaire',
            field=models.OneToOneField(null=True, blank=True, to='feedback.AnswerSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='target',
            field=models.ForeignKey(to='events.Event'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('applicant', 'target')]),
        ),
        migrations.CreateModel(
            name='IncomingApplication',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('events.application',),
        ),
        migrations.CreateModel(
            name='OutgoingApplication',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('events.application',),
        ),
    ]
