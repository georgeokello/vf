# Generated by Django 4.2.10 on 2024-03-25 17:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_alter_activity_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundiuser',
            name='classTaught',
            field=models.CharField(default=datetime.datetime(2024, 3, 25, 17, 46, 0, 48973, tzinfo=datetime.timezone.utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fundiuser',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
