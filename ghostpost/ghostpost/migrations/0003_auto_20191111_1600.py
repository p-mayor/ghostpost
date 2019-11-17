# Generated by Django 2.2.6 on 2019-11-11 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0002_auto_20191111_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upordown',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
