# Generated by Django 3.2.3 on 2021-05-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_remove_profile_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
