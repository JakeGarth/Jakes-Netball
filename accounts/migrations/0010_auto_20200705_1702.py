# Generated by Django 3.0.1 on 2020-07-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_advertisements_advertisementcompetiton'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='FillIn',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='Permanent',
            field=models.BooleanField(default=True),
        ),
    ]