# Generated by Django 4.0.6 on 2022-07-20 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dev_Content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dev_Title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dev_Type',
        ),
    ]
