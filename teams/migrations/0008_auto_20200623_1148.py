# Generated by Django 3.0.1 on 2020-06-23 01:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_teams_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='currentNumPlayers',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='teams',
            name='lookingGenderPlayers',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='lookingNumPlayers',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='teams',
            name='notes',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
