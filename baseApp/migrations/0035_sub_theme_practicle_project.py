# Generated by Django 4.2.10 on 2024-09-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0034_theme_sub_theme_chapters'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_theme',
            name='practicle_project',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
