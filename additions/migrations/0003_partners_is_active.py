# Generated by Django 3.1.1 on 2020-11-09 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additions', '0002_auto_20201109_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
