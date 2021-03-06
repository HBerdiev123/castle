# Generated by Django 3.1.1 on 2020-11-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_delete_myfavorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.profile')),
                ('priority', models.IntegerField()),
                ('occupation', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
                'ordering': ['-created_at'],
            },
            bases=('profiles.profile',),
        ),
    ]
