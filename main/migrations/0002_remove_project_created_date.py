# Generated by Django 3.2.8 on 2021-11-05 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_date',
        ),
    ]
