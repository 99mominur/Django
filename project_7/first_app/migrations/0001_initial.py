# Generated by Django 4.1.2 on 2023-08-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('fathers_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]