# Generated by Django 3.0.14 on 2021-11-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20201121_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='title',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]