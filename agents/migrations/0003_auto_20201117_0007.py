# Generated by Django 3.1.1 on 2020-11-17 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20201117_0002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='occpupation',
            new_name='occupation',
        ),
    ]
