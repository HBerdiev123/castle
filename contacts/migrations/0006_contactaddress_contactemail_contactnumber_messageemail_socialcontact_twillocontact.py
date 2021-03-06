# Generated by Django 3.0.11 on 2020-11-26 09:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0005_auto_20201125_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('region', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('postalcode', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message_email', models.CharField(max_length=100)),
                ('email_host', models.CharField(max_length=100)),
                ('email_port', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('social_url', models.CharField(max_length=150)),
                ('social_icon', models.CharField(blank=True, max_length=150)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwilloContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('twillo_account', models.CharField(max_length=100)),
                ('twillo_token', models.CharField(max_length=100)),
                ('twillo_number', models.CharField(max_length=100)),
                ('default_twillo', models.CharField(blank=True, default=False, max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
