# Generated by Django 4.1.2 on 2023-06-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=30),
        ),
    ]
