# Generated by Django 5.1.4 on 2025-02-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_judge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event/judges/'),
        ),
    ]
