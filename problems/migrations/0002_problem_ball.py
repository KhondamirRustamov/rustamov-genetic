# Generated by Django 3.2.3 on 2021-05-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='ball',
            field=models.IntegerField(default=0),
        ),
    ]
