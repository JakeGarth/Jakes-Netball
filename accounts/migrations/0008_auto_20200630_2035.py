# Generated by Django 3.0.1 on 2020-06-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_advertisements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
