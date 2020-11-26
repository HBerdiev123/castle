# Generated by Django 3.1.1 on 2020-11-25 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0004_emails_is_replied'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='is_checked',
        ),
        migrations.RemoveField(
            model_name='emails',
            name='is_replied',
        ),
        migrations.RemoveField(
            model_name='emails',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='emailtoagent',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailtoagent',
            name='is_replied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailtoagent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='ReplyLetter',
            fields=[
                ('emails_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.emails')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('contacts.emails',),
        ),
    ]