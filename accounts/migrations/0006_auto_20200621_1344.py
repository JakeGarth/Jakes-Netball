# Generated by Django 3.0.1 on 2020-06-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_accounts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='gender',
            field=models.CharField(default='Female', max_length=10),
        ),
    ]
