# Generated by Django 4.2.10 on 2024-04-01 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0009_videoactivity_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoactivity',
            name='video_or_image_name',
            field=models.CharField(default=datetime.datetime(2024, 4, 1, 9, 15, 53, 812420, tzinfo=datetime.timezone.utc), max_length=1500),
            preserve_default=False,
        ),
    ]
