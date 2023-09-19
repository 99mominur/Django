# Generated by Django 4.1.2 on 2023-06-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_school_fathers_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]