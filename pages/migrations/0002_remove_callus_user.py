# Generated by Django 5.0.7 on 2024-07-19 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callus',
            name='user',
        ),
    ]
