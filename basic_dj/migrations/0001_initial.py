# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-09 09:53
from __future__ import unicode_literals

import basic_dj.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=4)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('authors', models.ManyToManyField(related_name='books', to='basic_dj.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('publisher_file', models.FileField(upload_to=basic_dj.storage.upload_document)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='basic_dj.Publisher'),
        ),
    ]