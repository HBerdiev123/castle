# Generated by Django 3.1.1 on 2020-10-12 16:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0002_auto_20201012_1353'),
        ('profiles', '0003_auto_20201012_1633'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyFavorities',
            new_name='MyFavorites',
        ),
    ]
