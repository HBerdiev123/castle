# Generated by Django 3.1.1 on 2020-11-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additions', '0003_partners_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='partner_name',
            field=models.CharField(max_length=120),
        ),
    ]
