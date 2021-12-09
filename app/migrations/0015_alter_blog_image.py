# Generated by Django 3.2.9 on 2021-12-09 10:32

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='blogimg'),
        ),
    ]