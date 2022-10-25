# Generated by Django 4.1.1 on 2022-10-22 04:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_create_date_alter_post_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 4, 11, 21, 764980, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 22, 4, 11, 21, 765480, tzinfo=datetime.timezone.utc)),
        ),
    ]