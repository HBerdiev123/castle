# Generated by Django 3.1.1 on 2020-11-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='agents')),
                ('about_agent', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Agents',
            },
        ),
    ]
