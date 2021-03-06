# Generated by Django 3.1.1 on 2020-11-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_property_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_prop', to='property.property')),
            ],
        ),
    ]
