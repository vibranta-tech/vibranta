# Generated by Django 5.1.4 on 2025-02-05 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
