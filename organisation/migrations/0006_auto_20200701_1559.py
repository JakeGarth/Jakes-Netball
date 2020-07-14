# Generated by Django 3.0.1 on 2020-07-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0005_competitions'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitions',
            name='CompetitionGrade',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='CompetitionGender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Either', 'Either')], default='Either', max_length=6),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='CompetitionLocation',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='organisations',
            name='OrganisationName',
            field=models.CharField(default=None, max_length=30, unique=True),
        ),
    ]
