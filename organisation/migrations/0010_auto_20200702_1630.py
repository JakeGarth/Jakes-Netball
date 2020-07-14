# Generated by Django 3.0.1 on 2020-07-02 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0009_remove_competitions_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitions',
            name='CompetitionRegistrationLink',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='CompetitionEndDate',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='CompetitionStartDate',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='LengthOfGame',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]