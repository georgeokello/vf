# Generated by Django 4.2.10 on 2024-04-23 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0017_remove_session_topiccode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundiuser',
            name='classTaught',
        ),
    ]
