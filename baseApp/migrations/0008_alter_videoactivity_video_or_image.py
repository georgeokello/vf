# Generated by Django 4.2.10 on 2024-04-01 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_remove_activity_activityname_remove_activity_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoactivity',
            name='video_or_image',
            field=models.FileField(upload_to='uploaded_files'),
        ),
    ]
