# Generated by Django 3.2.7 on 2021-11-22 09:39

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_auto_20211120_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupstructure',
            name='group_id',
            field=models.CharField(default=chat.models.GroupIdCreator, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='groupstructure',
            name='link',
            field=models.CharField(default=chat.models.GroupLinkCreator, editable=False, max_length=100, unique=True),
        ),
    ]
