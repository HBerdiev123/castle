# Generated by Django 3.1.1 on 2020-10-14 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201012_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myfavorites',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='myfavorites',
            old_name='date_udpated',
            new_name='updated_at',
        ),
    ]
