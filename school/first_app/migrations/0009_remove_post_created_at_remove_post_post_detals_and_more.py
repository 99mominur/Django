# Generated by Django 4.1.2 on 2023-06-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0008_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_detals',
        ),
        migrations.AddField(
            model_name='post',
            name='post_details',
            field=models.CharField(default='Post details', max_length=500),
        ),
    ]
