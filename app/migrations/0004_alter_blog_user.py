# Generated by Django 3.2.9 on 2021-12-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.IntegerField(),
        ),
    ]
