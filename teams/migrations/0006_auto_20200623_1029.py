# Generated by Django 3.0.1 on 2020-06-23 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_teams_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='endTimeRange',
            field=models.TimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='startTimeRange',
            field=models.TimeField(default=None, null=True),
        ),
    ]
