# Generated by Django 2.1.7 on 2019-03-15 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0004_auto_20190315_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudents',
            name='id',
            field=models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
