# Generated by Django 5.2.3 on 2025-06-20 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwinProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_priorities', models.JSONField(default=list)),
                ('interests', models.JSONField(default=list)),
                ('brand_affinities', models.JSONField(default=list)),
                ('price_sensitivity', models.JSONField(default=list)),
                ('shopping_frequency', models.CharField(default=3)),
                ('vibe', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='twin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
