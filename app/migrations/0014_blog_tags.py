# Generated by Django 3.2.9 on 2021-12-03 10:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_user_id_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), null=True, size=None),
        ),
    ]
