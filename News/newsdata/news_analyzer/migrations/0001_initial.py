# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=100)),
                ('article_date', models.CharField(max_length=50)),
                ('article_source', models.CharField(max_length=20)),
                ('article_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.AutoField(primary_key=True, serialize=False)),
                ('keyword_word', models.CharField(max_length=50)),
            ],
        ),
    ]
