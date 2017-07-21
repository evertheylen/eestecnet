# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to=b'entryimages')),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default=b'news', max_length=20, choices=[(b'news', b'EESTEC News'), (b'carreer', b'Carreer Offer')])),
                ('published', models.BooleanField(default=False)),
                ('front_page_news', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('privileged', models.BooleanField(default=False)),
                ('board', models.BooleanField(default=False)),
                ('alumni', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
