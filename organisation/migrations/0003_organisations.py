# Generated by Django 3.0.1 on 2020-06-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0004_remove_teams_teams'),
        ('organisation', '0002_delete_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganisationName', models.CharField(default=None, max_length=100)),
                ('teams', models.ManyToManyField(to='teams.Teams')),
            ],
        ),
    ]
