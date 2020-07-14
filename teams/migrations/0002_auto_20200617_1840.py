# Generated by Django 3.0.1 on 2020-06-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='dates',
            field=models.CharField(default='Session 2', max_length=100),
        ),
        migrations.AddField(
            model_name='teams',
            name='day',
            field=models.CharField(default='Monday', max_length=100),
        ),
        migrations.AddField(
            model_name='teams',
            name='lengthOfGame',
            field=models.CharField(default='1 hour', max_length=100),
        ),
        migrations.AddField(
            model_name='teams',
            name='location',
            field=models.CharField(default='MQ Gym', max_length=100),
        ),
        migrations.AddField(
            model_name='teams',
            name='startTimeRange',
            field=models.CharField(default='6pm', max_length=100),
        ),
        migrations.AlterField(
            model_name='teams',
            name='teamName',
            field=models.CharField(default="Jake's Team", max_length=100),
        ),
    ]