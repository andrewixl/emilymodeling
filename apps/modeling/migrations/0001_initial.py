# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=25)),
                ('album_location', models.CharField(max_length=25)),
                ('album_description', models.CharField(max_length=50)),
                ('shoot_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='media/None/no-img.jpg', upload_to='media/')),
                ('photo_caption', models.CharField(max_length=25)),
                ('photo_description', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('master_album', models.ManyToManyField(related_name='album', to='modeling.Album')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='slide_1',
            field=models.ManyToManyField(related_name='slide_1', to='modeling.Photo'),
        ),
        migrations.AddField(
            model_name='home',
            name='slide_2',
            field=models.ManyToManyField(related_name='slide_2', to='modeling.Photo'),
        ),
        migrations.AddField(
            model_name='home',
            name='slide_3',
            field=models.ManyToManyField(related_name='slide_3', to='modeling.Photo'),
        ),
        migrations.AddField(
            model_name='home',
            name='slide_4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeling.Photo'),
        ),
    ]
