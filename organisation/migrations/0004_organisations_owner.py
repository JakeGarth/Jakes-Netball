# Generated by Django 3.0.1 on 2020-06-21 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200621_1344'),
        ('organisation', '0003_organisations'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisations',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Accounts'),
        ),
    ]
