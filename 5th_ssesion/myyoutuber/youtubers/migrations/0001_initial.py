# Generated by Django 3.0.6 on 2020-05-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='youtubers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelname', models.CharField(max_length=100)),
                ('creatorname', models.CharField(max_length=100)),
                ('preference', models.IntegerField()),
                ('onair', models.BooleanField()),
                ('subscribers', models.IntegerField()),
                ('link1', models.TextField()),
                ('link2', models.TextField()),
                ('link3', models.TextField()),
            ],
        ),
    ]