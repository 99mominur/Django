# Generated by Django 4.1.2 on 2023-06-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='fathers_name',
            field=models.TextField(default='Abdullah'),
        ),
    ]
