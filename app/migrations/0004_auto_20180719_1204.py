# Generated by Django 2.0.7 on 2018-07-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(max_length=25, unique=True),
        ),
    ]
