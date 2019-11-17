# Generated by Django 2.2.6 on 2019-11-11 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='boast',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.CharField(max_length=280),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
