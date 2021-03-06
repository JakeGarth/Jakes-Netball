# Generated by Django 3.0.1 on 2020-06-19 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisation', '0003_organisations'),
        ('teams', '0004_remove_teams_teams'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisationsJoined', models.ManyToManyField(related_name='AccountOrgsJoined', to='organisation.Organisations')),
                ('organisationsMade', models.ManyToManyField(related_name='AccountOrgsMade', to='organisation.Organisations')),
                ('teamsJoined', models.ManyToManyField(related_name='AccountTeamsJoined', to='teams.Teams')),
                ('teamsMade', models.ManyToManyField(related_name='AccountTeamsMade', to='teams.Teams')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
