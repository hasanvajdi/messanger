# Generated by Django 3.2.7 on 2021-11-20 10:55

import chat.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0007_auto_20211120_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstructure',
            name='admins',
            field=models.ManyToManyField(blank=True, default=chat.models.current_user, null=True, related_name='group_admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='groupstructure',
            name='members',
            field=models.ManyToManyField(blank=True, default=chat.models.current_user, null=True, related_name='group_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
