# Generated by Django 2.1.7 on 2019-03-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalstudentinfo',
            name='photo_value',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='photo_value',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]
