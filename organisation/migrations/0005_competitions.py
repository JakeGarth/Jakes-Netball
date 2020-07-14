# Generated by Django 3.0.1 on 2020-06-30 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200630_2035'),
        ('teams', '0009_teams_org'),
        ('organisation', '0004_organisations_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompetitionDay', models.CharField(default=None, max_length=10)),
                ('CompetitionSport', models.CharField(default=None, max_length=25)),
                ('CompetitionGender', models.CharField(default=None, max_length=10)),
                ('CompetitionLocation', models.CharField(default='MQ Gym', max_length=100)),
                ('LengthOfGame', models.CharField(default='1 hour', max_length=100)),
                ('CompetitionStartTime', models.TimeField(default=None, null=True)),
                ('CompetitionEndTime', models.TimeField(default=None, null=True)),
                ('CompetitionOrganisation', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisations')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Accounts')),
                ('teams', models.ManyToManyField(to='teams.Teams')),
            ],
        ),
    ]
