# Generated by Django 3.2.4 on 2023-11-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='post',
            name='commentsCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likesCount',
            field=models.IntegerField(default=0),
        ),
    ]
