# Generated by Django 3.1.7 on 2021-08-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EQuest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='content1',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='content2',
            field=models.TextField(default=None),
        ),
    ]
