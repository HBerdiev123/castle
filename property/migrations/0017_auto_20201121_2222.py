# Generated by Django 3.1.1 on 2020-11-21 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20201118_2238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-created']},
        ),
    ]
